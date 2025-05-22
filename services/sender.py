# services/sender.py

import requests

def send_embedding_to_api(document_id: str, embedding: list[float], metadata: dict):
    #Cambio en esta linea para que me funcione con la otra api 
    url = "http://api-load:8002/store_embedding" 
    payload = {
        "id": document_id,
        "embedding": embedding,
        "metadata": metadata
    }
    print(f"🔁 Enviando embedding con ID: {document_id}")
    print(f"🧠 Longitud del embedding: {len(embedding)}")
    print(f"📦 Metadata: {metadata}")

    
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Lanza excepción si hay error HTTP
    return response.json() # Devuelve la respuesta de la API
