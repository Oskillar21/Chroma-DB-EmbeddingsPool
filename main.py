from utils.file_loader import load_documents_from_folder
from embeddings.generator import Embedder
from database.chroma_client import get_chroma_client, get_or_create_collection

# Cargar documentos desde carpeta
documents = load_documents_from_folder("data")
print(f"📄 Documentos encontrados: {len(documents)}")
print(f"-------------------------------")

# Inicializar modelo de embeddings
embedder = Embedder()

# Inicializar cliente de Chroma
client = get_chroma_client()
collection = get_or_create_collection(client)

# Procesar documentos y guardar embeddings
for file_name, content in documents:
    print(f"🔍 Procesando {file_name}")
    embedding = embedder.embed([content])[0]
    print(f"Embedding generado para {file_name}: {embedding[:5]}")  # Resumen del embedding
    try:
        collection.add(
            documents=[content],
            embeddings=[embedding],
            ids=[file_name]
        )
        print(f"Documento: {file_name} agregado a la colección.")
        print(f"-------------------------------")
    except Exception as e:
        print(f"⚠️ Error al agregar {file_name} a la colección: {e}")

# Guardar la colección en Chroma y finalizacion del proceso
print("✅ Proceso de indexación completado.")


