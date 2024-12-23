import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def process_query(query):
    # Preprocess query
    tokens = word_tokenize(query)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(word) for word in filtered_tokens]
    
    return stemmed_tokens

def get_documents(doc_ids):
    with open('data.json', 'r') as f:
        data = json.load(f)
    return [data[doc_id]['content'] for doc_id in doc_ids]

def search(query, method="boolean"):
    query_tokens = process_query(query)
    
    if method == "boolean":
        from ranking import boolean_retrieval
        doc_ids = boolean_retrieval(query_tokens)
    elif method == "vsm":
        from ranking import vector_space_model
        doc_ids = vector_space_model(query_tokens)
    elif method == "bm25":
        from ranking import bm25
        doc_ids = bm25(query_tokens)
    else:
        raise ValueError("Unknown method: {}".format(method))
    
    documents = get_documents(doc_ids)
    return documents

if __name__ == "__main__":
    query = "web scraping"
    method = "boolean"  # Change to "vsm" or "bm25" as needed
    results = search(query, method)
    print(f"Results for '{query}': {results}")
