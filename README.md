
---

### 📚 `Chroma-DB-EmbeddingsPool` → `README.md`

```markdown
# Chroma-DB-EmbeddingsPool

Servicio en FastAPI que permite cargar documentos y generar embeddings utilizando `sentence-transformers`, para luego almacenarlos en ChromaDB. Ideal para pruebas o proyectos pequeños.

## Características

- Procesamiento de PDFs, DOCX y otros
- Generación de embeddings con modelos de lenguaje
- Almacenamiento en base de datos vectorial ChromaDB

## Instalación y uso

```bash
# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el servidor
uvicorn main:app --reload --port 8001
