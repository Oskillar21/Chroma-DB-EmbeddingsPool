import chromadb

def get_chroma_client():
    return chromadb.PersistentClient(path="./chroma_db")

def get_or_create_collection(client, collection_name="default"):
    return client.get_or_create_collection(name=collection_name)
