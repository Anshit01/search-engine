# Search engine
My shiny new search engine built using the concepts of Information Retrieval.

## Steps to run
### Crawl and scrap
We crawl all the urls of countries from wikipedia's article on countries
https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_area

Then the retrieved urls are scrapped for text content using beautiful soup.
```
python crawler.py
```

### Index documents
In this step we build the positional inverted index using the retrieved documents.
```
python indexer.py
```
`index.json` file will be created with the positional index saved in json format for later use.

### Search using queries
Now the index is built, so we can run our search engine to perform queries on it.
```
python search_engine.py
```
