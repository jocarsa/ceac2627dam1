import requests
import chromadb

cliente = chromadb.PersistentClient(path="./chromadb")
coleccion = cliente.get_collection("libros")

pregunta = input("Introduce tu pregunta: ")

r = requests.post(
    "http://localhost:11434/api/embed",
    json={
        "model": "nomic-embed-text:latest",
        "input": pregunta
    }
)

embedding = r.json()["embeddings"][0]

resultados = coleccion.query(
    query_embeddings=[embedding],
    n_results=5
)

for texto, distancia in zip(
    resultados["documents"][0],
    resultados["distances"][0]
):
    print("Distancia:", distancia)
    print("Texto:", texto)
    print("-" * 50)