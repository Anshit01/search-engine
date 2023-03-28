import json
from collections import OrderedDict
import re
import copy


# {term: {doc_id: [positions]}}}
with open("index.json") as f:
    index = json.load(f)

# for single word query
while True:
    query = input("Enter your query: ").split()
    
    phrase_res = copy.deepcopy(index.get(query[0], {}))
    term_i = 1
    for term in query[1:]:
        term_res = index[term]  # {doc_id: [positions]}
        for doc_id in list(phrase_res.keys()):
            if doc_id in term_res:
                merged_list = []
                for pos in phrase_res[doc_id]:
                    if pos + term_i in term_res[doc_id]:
                        merged_list.append(pos)
                if merged_list:
                    phrase_res[doc_id] = merged_list
                else:
                    del phrase_res[doc_id]
            else:
                del phrase_res[doc_id]
        term_i += 1

    total_docs = len(phrase_res)
    if total_docs == 0:
        print("No results were found.")
        continue
    
    doc_freq = {}
    for doc in phrase_res:
        doc_freq[doc] = len(phrase_res[doc])

    doc_freq_sorted = OrderedDict(sorted(doc_freq.items(), key=lambda kv: kv[1], reverse=True))
    
    # printing final results
    print(f"{total_docs} results were found")
    print("------------------------------")
    i = 1
    for key, value in doc_freq_sorted.items():
        print(f"{i}) {key} [appears {value} times]")
        term_positions = phrase_res[key]
        content1 = None
        content2 = None

        with open(f"database/{key}.json") as f:
            doc = json.load(f)
            terms = [term.lower() for term in re.split(r"\W+", doc["content"]) if term != "" and term.isnumeric() == False]
            content1 = terms[term_positions[0] - 5 : term_positions[0] + 5]
            if len(term_positions) > 1:
                content2 = terms[term_positions[1] - 5 : term_positions[1] + 5]

        print(doc['url'])
        print(f"...{' '.join(content1)}...")
        if content2:
            print(f"...{' '.join(content2)}...")

        print("")

        i += 1
