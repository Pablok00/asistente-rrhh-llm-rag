from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path
import os
from dotenv import load_dotenv


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT_DIR / "data"
FAISS_DIR = ROOT_DIR / "faiss_index"
ENV_PATH = ROOT_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


def cargar_documentos_txt(ruta_base):
    documentos = []
    ruta = Path(ruta_base)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró la carpeta de datos: {ruta}")

    for archivo in ruta.rglob("*.txt"):
        loader = TextLoader(str(archivo), encoding="utf-8")
        documentos.extend(loader.load())

    return documentos


def crear_base_vectorial():
    github_token = os.getenv("GITHUB_TOKEN")

    if not github_token:
        raise ValueError("No se encontró GITHUB_TOKEN en el archivo .env")

    documentos = cargar_documentos_txt(DATA_DIR)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documentos)

    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small",
        api_key=github_token,
        base_url="https://models.inference.ai.azure.com"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(str(FAISS_DIR))

    print("Base vectorial creada correctamente.")
    print(f"Cantidad de documentos cargados: {len(documentos)}")
    print(f"Cantidad de fragmentos generados: {len(chunks)}")


if __name__ == "__main__":
    crear_base_vectorial()
