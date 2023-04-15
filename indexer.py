import json
import re
from os import listdir
import time

start  = time.time()
index = {} # {term: {doc_id: [positions]}}}

print("Loading documents and building index...")

docs = [doc for doc in listdir("database") if doc.endswith(".json")]

for doc in docs:
    with open(f"database/{doc}") as f:
        data = json.load(f)
        doc_id = data["name"]
        content = data["content"]

        # Tokenization with case folding, punctuation removal and number removal
        terms = [term.lower() for term in re.split(r"\W+", content) if term != "" and term.isnumeric() == False]
        
        # Building positional inverted index
        for i, term in enumerate(terms):
            if term not in index:
                index[term] = {}
            if doc_id not in index[term]:
                index[term][doc_id] = []
            index[term][doc_id].append(i)

print("Index built!")
print("Saving index to file...")

# Save the index to a file
with open("index.json", "w") as f:
    json.dump(index, f)

print("Index saved to index.json")
print(f"Time taken: {time.time() - start}")
