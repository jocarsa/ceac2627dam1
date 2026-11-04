import requests
import chromadb			 # Si no tenéis chroma: pip3 install chromadb --break-system-packages

ruta = "http://localhost:11434/api/embed"
modelo = "nomic-embed-text:latest"

# Texto
pregunta = "estoy viviendo en Valencia"

# Generar embedding con Ollama
r = requests.post(ruta, json={
    "model": modelo,
    "input": pregunta
})
r.raise_for_status()

respuesta = r.json()["embeddings"][0]

# Conectar con ChromaDB (persistente)
cliente = chromadb.PersistentClient(path="./chromadb")

# Crear colección si no existe
coleccion = cliente.get_or_create_collection(name="memoria")

# Guardar embedding
coleccion.add(
    ids=["1"],
    embeddings=[respuesta],
    documents=[pregunta]
)

print("Embedding guardado correctamente")