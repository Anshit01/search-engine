import re

content = "India, officially the Republic of India (Hindi: Bh\u0101rat Ga\u1e47ar\u0101jya),[25] is a country in South Asia. It is the seventh-largest country by area and the second-most populous country."

terms = [term.lower() for term in re.split(r"\W+", content) if term != "" and term.isnumeric() == False]

print(' '.join(terms))