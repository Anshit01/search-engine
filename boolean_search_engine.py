import pandas as pd
import time

start = time.time()
index = pd.read_csv("boolean_index.csv", index_col=0)
doc_names = list(index.columns)
print("Index loaded in", time.time() - start, "seconds")

while True:
    query = input("Enter your query: ").split()

    resultant_posting = index.loc[query[0]]
    
    for term in query[1:]:
        resultant_posting = resultant_posting & index.loc[term]

    resultant_docs = resultant_posting[resultant_posting == 1].index.tolist()

    if len(resultant_docs) == 0:
        print("No results were found.")
        continue
    
    # printing final results
    print(f"{len(resultant_docs)} results were found")
    print("------------------------------")
    for i, doc_name in enumerate(resultant_docs):
        print(f"{i + 1}) {doc_name}")
