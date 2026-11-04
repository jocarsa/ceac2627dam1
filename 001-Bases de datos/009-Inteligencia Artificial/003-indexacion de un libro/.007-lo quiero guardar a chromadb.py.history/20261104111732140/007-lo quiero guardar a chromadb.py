import requests
import chromadb

# ChromaDB
cliente = chromadb.PersistentClient(path="./chromadb")
coleccion = cliente.get_or_create_collection("libros")

# Ollama
ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"

# Documento
archivo = open("Publicado - Aprende programación con Python.md", "r")
documento = archivo.read()
archivo.close()

# Fragmentación
cacho = 4000
solapado = 100

for i in range(0, len(documento), cacho - solapado):

    cachodocumento = documento[i:i+cacho]

    # Obtener embedding
    r = requests.post(ruta, json={
        "model": modelo,
        "input": cachodocumento
    })
    r.raise_for_status()

    respuesta = r.json()["embeddings"][0]

    # Guardar en ChromaDB
    coleccion.upsert(
        ids=[f"fragmento_{i}"],
        documents=[cachodocumento],
        embeddings=[respuesta],
        metadatas=[{
            "archivo": "Publicado - Aprende programación con Python.md",
            "posicion": i
        }]
    )

    print(f"Guardado fragmento {i}: {cachodocumento[:40]}")

print("Total de fragmentos:", coleccion.count())