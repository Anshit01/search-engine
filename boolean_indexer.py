import json
import re
from os import listdir
import time

start = time.time()
index = {} # {term: [0|1, ...]}
doc_names = []

print("Loading documents and building index...")

docs = [doc for doc in listdir("database") if doc.endswith(".json")]

for i, doc in enumerate(docs):
    with open(f"database/{doc}") as f:
        data = json.load(f)
        doc_id = data["name"]
        content = data["content"]

        if (doc_id.count(',')):
            doc_id = doc_id.replace(',', '')

        # Tokenization with case folding, punctuation removal and number removal
        terms = [term.lower() for term in re.split(r"\W+", content) if term != "" and term.isnumeric() == False]
        
        doc_names.append(doc_id)

        # Building boolean retrieval matrix
        for term in terms:
            if term not in index:
                index[term] = [0] * len(docs)
            index[term][i] = 1

print("Index built!")
print("Saving index to file...")

# Save the index to a file
csv = f",{','.join(doc_names)}\n"
for term, postings in index.items():
    csv += f"{term},{','.join([str(p) for p in postings])}\n"

with open("boolean_index.csv", "w") as f:
    f.write(csv)

print("Index saved to boolean_index.json")
print(f"Time taken: {time.time() - start}")