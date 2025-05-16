# main.py

from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from utils.file_loader import extract_text_from_pdf, extract_text_from_docx
from embeddings.generator import Embedder
from services.sender import send_embedding_to_api

app = FastAPI()
embedder = Embedder()

@app.post("/process-documents")
async def process_documents(file: UploadFile = File(...)):
    try:
        # Verifica extensión
        if not (file.filename.endswith(".pdf") or file.filename.endswith(".docx")):
            raise HTTPException(status_code=400, detail="Tipo de archivo no soportado")

        # Lee contenido del archivo
        contents = await file.read()
        with open(f"temp_{file.filename}", "wb") as f:
            f.write(contents)

        # Extrae texto
        if file.filename.endswith(".pdf"):
            text = extract_text_from_pdf(f"temp_{file.filename}")
        else:
            text = extract_text_from_docx(f"temp_{file.filename}")

        # Genera embedding
        embedding = embedder.embed([text])[0]

        # Metadata opcional
        metadata = {
            "filename": file.filename,
            "length": str(len(text))
        }

        # Envía a segunda API
        response = send_embedding_to_api(file.filename, embedding, metadata)

        return JSONResponse(content={"message": "Embedding procesado y enviado", "response": response})

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
