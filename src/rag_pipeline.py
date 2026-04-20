import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


ROOT_DIR = Path(__file__).resolve().parent.parent
FAISS_DIR = ROOT_DIR / "faiss_index"
ENV_PATH = ROOT_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


PROMPT_SISTEMA = """
Eres un asistente interno de recursos humanos de Comercial Andina SpA, una empresa de servicios.
Tu función es responder consultas frecuentes de los trabajadores sobre vacaciones,
permisos administrativos, licencias médicas, beneficios, horarios y normativas internas.

Debes responder únicamente en base a la información entregada por los documentos recuperados.
Si la información no es suficiente, debes indicarlo claramente y sugerir que la consulta
sea revisada por el área de recursos humanos.

Usa un lenguaje formal, claro, preciso y fácil de comprender.
No inventes información.
No incluyas saludos, despedidas, firmas ni campos de plantilla como "[Su Nombre]".
"""


def _formatear_fuente(fuente: str) -> str:
    ruta = Path(fuente)

    try:
        return str(ruta.resolve().relative_to(ROOT_DIR)).replace("\\", "/")
    except ValueError:
        return str(ruta)


def _obtener_fuentes(documentos):
    fuentes = []

    for documento in documentos:
        fuente = documento.metadata.get("source")

        if fuente:
            fuente_formateada = _formatear_fuente(fuente)

            if fuente_formateada not in fuentes:
                fuentes.append(fuente_formateada)

    return fuentes


def _limpiar_formato_carta(texto: str) -> str:
    lineas_no_permitidas = {
        "estimado/a,",
        "estimado/a",
        "atentamente,",
        "atentamente",
        "[su nombre]",
        "asistente de recursos humanos",
        "comercial andina spa",
    }

    lineas_limpias = []

    for linea in texto.splitlines():
        linea_normalizada = linea.strip().lower()

        if linea_normalizada in lineas_no_permitidas:
            continue

        lineas_limpias.append(linea)

    return "\n".join(lineas_limpias).strip()


def responder_consulta(pregunta: str) -> str:
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        raise ValueError("No se encontró GITHUB_TOKEN en el archivo .env")

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=github_token,
        base_url="https://models.inference.ai.azure.com"
    )

    if not FAISS_DIR.exists():
        raise FileNotFoundError(
            "No se encontró la base vectorial. Ejecuta primero: python src\\crear_vectores.py"
        )

    vectorstore = FAISS.load_local(
        str(FAISS_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )

    documentos_relevantes = vectorstore.similarity_search(pregunta, k=3)
    contexto = "\n\n".join([doc.page_content for doc in documentos_relevantes])

    prompt_final = f"""
{PROMPT_SISTEMA}

Consulta del usuario:
{pregunta}

Contexto recuperado:
{contexto}

Responde de forma breve, clara y ordenada.
No uses formato de carta, no firmes la respuesta y no incluyas placeholders.
"""

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        api_key=github_token,
        base_url="https://models.inference.ai.azure.com"
    )

    respuesta = llm.invoke(prompt_final)
    contenido_respuesta = _limpiar_formato_carta(respuesta.content)
    fuentes = _obtener_fuentes(documentos_relevantes)

    if not fuentes:
        return contenido_respuesta

    fuentes_texto = "\n".join([f"- {fuente}" for fuente in fuentes])

    return f"{contenido_respuesta}\n\nFuentes consultadas:\n{fuentes_texto}"


if __name__ == "__main__":
    pregunta = input("Ingresa tu consulta: ")
    respuesta = responder_consulta(pregunta)
    print("\nRespuesta del asistente:\n")
    print(respuesta)
