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

1. Busca información relevante en documentos.
2. Recupera el contexto más útil.
3. Genera una respuesta basada en esos datos.
4. Muestra las fuentes consultadas para respaldar la respuesta.

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
- `data/internos/`: documentos internos.
- `data/externos/`: documentos externos.
- `src/`: lógica del sistema.
- `evidencias/`: capturas de pruebas.
- `app.py`: archivo principal.
- `requirements.txt`: dependencias.

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

Desde este paso, todos los comandos deben ejecutarse dentro de la carpeta del proyecto.

Para comprobarlo en Windows, puedes usar:

```bash
dir
```

Deberías ver archivos como `app.py`, `README.md` y `requirements.txt`.

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

Cuando el entorno virtual esté activo, la terminal debería mostrar algo parecido a `(venv)` al inicio de la línea.

#### Error común en Windows
Si en Windows aparece un error como:

```bash
No se puede cargar el archivo porque la ejecución de scripts está deshabilitada en este sistema
```

Debes habilitar la ejecución de scripts de PowerShell:

1. Abrir PowerShell como administrador.
2. Ejecutar el siguiente comando:

```bash
Set-ExecutionPolicy RemoteSigned
```

3. Confirmar escribiendo `S` y presionar Enter.
4. Cerrar y abrir nuevamente la terminal de VS Code.
5. Volver a activar el entorno virtual:

```bash
.\venv\Scripts\Activate.ps1
```

---

### 6. Instalar dependencias
```bash
python -m pip install -r requirements.txt
```

Si aparece un error indicando que no encuentra `requirements.txt`, normalmente significa que la terminal no está ubicada dentro de la carpeta del proyecto.

Primero verifica la ubicación:

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

También puedes instalar usando la ruta completa del archivo. En ese caso, copia la ruta real donde descargaste el proyecto y úsala entre comillas:

```bash
python -m pip install -r "C:\Users\TU_USUARIO\Desktop\asistente-rrhh-llm-rag\requirements.txt"
```

---

## Configuración del archivo `.env`
Crear un archivo llamado `.env` en la raíz del proyecto con el siguiente contenido:

```env
GITHUB_TOKEN=TU_TOKEN_AQUI
OPENAI_BASE_URL=https://models.inference.ai.azure.com
```

**Importante:**
- Cada usuario debe usar su propio token de GitHub.
- No subir este archivo al repositorio.

---

## Ejecución del sistema

### 1. Crear base vectorial
Este paso es obligatorio antes de usar el sistema:

```bash
python src/crear_vectores.py
```

Si todo está correcto, el sistema mostrará la cantidad de documentos cargados y fragmentos generados.

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
- ¿La empresa entrega bonos por matrimonio?

---

## ¿Cómo funciona?
El sistema sigue este flujo:

1. El usuario hace una pregunta.
2. El sistema busca documentos relacionados en la base vectorial FAISS.
3. Se recupera el contexto más relevante.
4. El modelo genera una respuesta basada en ese contexto.
5. Se muestran la respuesta y las fuentes consultadas.

---

## Archivos importantes
- `src/crear_vectores.py`: genera la base vectorial.
- `src/rag_pipeline.py`: contiene la lógica del sistema RAG.
- `app.py`: ejecuta el asistente desde consola.
- `requirements.txt`: lista las dependencias necesarias.
- `README.md`: explica instalación, configuración y ejecución.

---

## Uso de IA
Se utilizó inteligencia artificial como apoyo en redacción y organización.
El diseño, lógica y desarrollo fueron realizados por el equipo.

---

## Autoría
Proyecto académico de la asignatura **Ingeniería de Soluciones con IA**.
