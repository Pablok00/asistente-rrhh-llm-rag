# Asistente Inteligente de RRHH con LLM y RAG

## Descripción
Este proyecto corresponde a un prototipo académico que utiliza inteligencia artificial para responder consultas frecuentes del área de recursos humanos.

Fue desarrollado para una empresa ficticia llamada **Comercial Andina SpA**, donde el área de RRHH recibe muchas preguntas repetitivas sobre vacaciones, permisos, licencias médicas y beneficios.

La solución combina un modelo de lenguaje (LLM) con un sistema de Recuperación Aumentada de Información (RAG), lo que permite responder preguntas basándose en documentos y no solo en conocimiento general.

---

## Objetivo
Diseñar un asistente capaz de responder consultas internas de forma clara, rápida y basada en información documentada.

---

## ¿Qué hace el sistema?
El sistema permite hacer preguntas en lenguaje natural y realiza lo siguiente:

1. Busca información relevante en documentos  
2. Recupera el contexto más útil  
3. Genera una respuesta basada en esos datos  

---

## Tecnologías utilizadas
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
- `src/`: lógica del sistema  
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

## Instalación paso a paso

### 1. Crear carpeta y abrir en VS Code
Primero crea una carpeta en tu computador y ábrela en Visual Studio Code.

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

---

### 4. Crear entorno virtual
```bash
python -m venv venv
```

---

### 5. Activar entorno virtual

**En Windows:**
```bash
venv\Scripts\activate
```

**En Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 6. Instalar dependencias
```bash
pip install -r requirements.txt
```

---

## Configuración del archivo `.env`

Crear un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```env
GITHUB_TOKEN=TU_TOKEN_AQUI
OPENAI_BASE_URL=https://models.inference.ai.azure.com
```

⚠️ **Importante:**
- Cada usuario debe usar su propio token de GitHub  
- No subir este archivo al repositorio  

---

## Ejecución del sistema

### 1. Crear base vectorial
Este paso es obligatorio antes de usar el sistema:

```bash
python src\crear_vectores.py
```

---

### 2. Ejecutar asistente
```bash
python app.py
```

---

## Ejemplos de preguntas

Puedes probar con:

- ¿Cuántos días de vacaciones tengo?  
- ¿Cómo se solicita un permiso?  
- ¿Qué hago con una licencia médica?  
- ¿Qué beneficios tiene la empresa?  

---

## ¿Cómo funciona?

El sistema sigue este flujo:

1. Usuario hace una pregunta  
2. Se buscan documentos relacionados  
3. Se recupera el contexto  
4. El modelo genera la respuesta  
5. Se muestra al usuario  

---

## Archivos importantes

- `crear_vectores.py`: genera la base vectorial  
- `rag_pipeline.py`: lógica del sistema RAG  
- `app.py`: ejecución del asistente  

---

## Uso de IA

Se utilizó inteligencia artificial como apoyo en redacción y organización.  
El diseño, lógica y desarrollo fueron realizados por el equipo.

---

## Autoría

Proyecto académico de la asignatura **Ingeniería de Soluciones con IA**
