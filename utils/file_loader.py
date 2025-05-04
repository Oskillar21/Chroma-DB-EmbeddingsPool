import os
import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(filepath):
    doc = fitz.open(filepath)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_text_from_docx(filepath):
    doc = docx.Document(filepath)
    return "\n".join([para.text for para in doc.paragraphs])

def load_documents_from_folder(folder_path):
    documents = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if file.endswith(".pdf"):
            text = extract_text_from_pdf(full_path)
        elif file.endswith(".docx"):
            text = extract_text_from_docx(full_path)
        else:
            continue
        documents.append((file, text))
    return documents
