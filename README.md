# Asistente Inteligente de RRHH con LLM y RAG

## DescripciÃ³n
Este proyecto corresponde a un prototipo acadÃ©mico que utiliza inteligencia artificial para responder consultas frecuentes del Ã¡rea de recursos humanos.

Fue desarrollado para una empresa ficticia llamada **Comercial Andina SpA**, donde el Ã¡rea de RRHH recibe muchas preguntas repetitivas sobre vacaciones, permisos, licencias mÃ©dicas y beneficios.

La soluciÃ³n combina un modelo de lenguaje (LLM) con un sistema de RecuperaciÃ³n Aumentada de InformaciÃ³n (RAG), lo que permite responder preguntas basÃ¡ndose en documentos y no solo en conocimiento general.

---

## Objetivo
DiseÃ±ar un asistente capaz de responder consultas internas de forma clara, rÃ¡pida y basada en informaciÃ³n documentada.

---

## Â¿QuÃ© hace el sistema?
El sistema permite hacer preguntas en lenguaje natural y realiza lo siguiente:

1. Busca informaciÃ³n relevante en documentos  
2. Recupera el contexto mÃ¡s Ãºtil  
3. Genera una respuesta basada en esos datos  

---

## TecnologÃ­as utilizadas
- Python  
- LangChain  
- FAISS  
- GitHub Models  
- Visual Studio Code  
- Git y GitHub  

---

## Estructura del proyecto
- `data/internos/`: documentos internos  
- `data/externos/`: documentos externos  
- `src/`: lÃ³gica del sistema  
- `evidencias/`: capturas de pruebas  
- `app.py`: archivo principal  
- `requirements.txt`: dependencias  

---

## Requisitos previos
Antes de comenzar, debes tener instalado:

- Python  
- Visual Studio Code  
- Git  

---

## InstalaciÃ³n paso a paso

### 1. Crear carpeta y abrir en VS Code
Primero crea una carpeta en tu computador y Ã¡brela en Visual Studio Code.

---

### 2. Clonar el repositorio
```bash
git clone https://github.com/Pablok00/asistente-rrhh-llm-rag.git
```

---

### 3. Entrar al proyecto
```bash
cd asistente-rrhh-llm-rag
```

Desde este paso, todos los comandos deben ejecutarse dentro de la carpeta del proyecto.  
Para comprobarlo en Windows, puedes usar:

```bash
dir
```

DeberÃ­as ver archivos como `app.py`, `README.md` y `requirements.txt`.

---

### 4. Crear entorno virtual
```bash
python -m venv venv
```

---

### 5. Activar entorno virtual

**En Windows PowerShell:**
```bash
.\venv\Scripts\Activate.ps1
```

**En Mac/Linux:**
```bash
source venv/bin/activate
```

Si en Windows aparece un error como:

### 6. Instalar dependencias
```bash
No se puede cargar el archivo porque la ejecuciÃ³n de scripts estÃ¡ deshabilitada en este sistema
```

Debes habilitar la ejecuciÃ³n de scripts de PowerShell:

1. Abrir PowerShell como administrador  
2. Ejecutar el siguiente comando:

```bash
Set-ExecutionPolicy RemoteSigned
```

3. Confirmar escribiendo `S` y presionar Enter  
4. Cerrar y abrir nuevamente la terminal de VS Code  
5. Volver a activar el entorno virtual:

```bash
.\venv\Scripts\Activate.ps1
```

Cuando el entorno virtual estÃ© activo, la terminal deberÃ­a mostrar algo parecido a `(venv)` al inicio de la lÃ­nea.

---

### 6. Instalar dependencias
```bash
python -m pip install -r requirements.txt
```

Si aparece un error indicando que no encuentra `requirements.txt`, normalmente significa que la terminal no estÃ¡ ubicada dentro de la carpeta del proyecto.

Primero verifica la ubicaciÃ³n:

```bash
dir
```

Si no ves el archivo `requirements.txt`, entra nuevamente a la carpeta:

```bash
cd asistente-rrhh-llm-rag
```

Luego intenta otra vez:

```bash
python -m pip install -r requirements.txt
```

TambiÃ©n puedes instalar usando la ruta completa del archivo. En ese caso, copia la ruta real donde descargaste el proyecto y Ãºsala entre comillas:

```bash
python -m pip install -r "C:\Users\TU_USUARIO\Desktop\asistente-rrhh-llm-rag\requirements.txt"
```

---

## ConfiguraciÃ³n del archivo `.env`

Crear un archivo llamado `.env` en la raÃ­z del proyecto con el siguiente contenido:

```env
GITHUB_TOKEN=TU_TOKEN_AQUI
OPENAI_BASE_URL=https://models.inference.ai.azure.com
```

 **Importante:**
- Cada usuario debe usar su propio token de GitHub  
- No subir este archivo al repositorio  

---

## EjecuciÃ³n del sistema

### 1. Crear base vectorial
Este paso es obligatorio antes de usar el sistema:

```bash
python src/crear_vectores.py
```

---

### 2. Ejecutar asistente
```bash
python app.py
```

---

## Ejemplos de preguntas

Puedes probar con:

- Â¿CuÃ¡ntos dÃ­as de vacaciones tengo?  
- Â¿CÃ³mo se solicita un permiso?  
- Â¿QuÃ© hago con una licencia mÃ©dica?  
- Â¿QuÃ© beneficios tiene la empresa?  

---

## Â¿CÃ³mo funciona?

El sistema sigue este flujo:

1. Usuario hace una pregunta  
2. Se buscan documentos relacionados  
3. Se recupera el contexto  
4. El modelo genera la respuesta  
5. Se muestra al usuario  

---

## Archivos importantes

- `crear_vectores.py`: genera la base vectorial  
- `rag_pipeline.py`: lÃ³gica del sistema RAG  
- `app.py`: ejecuciÃ³n del asistente  

---

## Uso de IA

Se utilizÃ³ inteligencia artificial como apoyo en redacciÃ³n y organizaciÃ³n.  
El diseÃ±o, lÃ³gica y desarrollo fueron realizados por el equipo.

---

## AutorÃ­a

Proyecto acadÃ©mico de la asignatura **IngenierÃ­a de Soluciones con IA**
