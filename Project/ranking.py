import json
from collections import Counter, defaultdict
import math

def boolean_retrieval(query_tokens):
    # Check for empty query
    if not query_tokens:
        return []
    
    try:
        # Load the index
        with open('index.json', 'r') as f:
            index = json.load(f)
    except FileNotFoundError:
        print("Error: index.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: index.json is not a valid JSON file.")
        return []
    
    # Initialize results with the postings of the first token
    first_token = query_tokens[0].lower()
    results = set(index.get(first_token, []))
    
    # Perform intersection for remaining tokens
    for token in query_tokens[1:]:
        token = token.lower()  # Ensure case-insensitivity
        results &= set(index.get(token, []))
    
    # Return sorted list of document IDs
    return sorted(results)

def vector_space_model(query_tokens):
    with open('preprocessed_data.json', 'r') as f:
        data = json.load(f)
    
    doc_vectors = defaultdict(lambda: [0] * len(query_tokens))
    query_vector = [0] * len(query_tokens)
    
    for i, token in enumerate(query_tokens):
        for doc_id, document in enumerate(data):
            token_counts = Counter(document['tokens'])
            query_vector[i] = token_counts[token]
            doc_vectors[doc_id][i] = token_counts[token]
    
    results = {}
    for doc_id, doc_vector in doc_vectors.items():
        similarity = cosine_similarity(query_vector, doc_vector)
        results[doc_id] = similarity
    
    return sorted(results.keys(), key=lambda x: results[x], reverse=True)

def cosine_similarity(vec1, vec2):
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
    magnitude2 = math.sqrt(sum(a ** 2 for a in vec2))
    if magnitude1 * magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)

def bm25(query_tokens, k1=1.5, b=0.75):
    with open('preprocessed_data.json', 'r') as f:
        data = json.load(f)
    
    N = len(data)  # Number of documents
    avgdl = sum(len(doc['tokens']) for doc in data) / N
    doc_lengths = {i: len(doc['tokens']) for i, doc in enumerate(data)}
    
    results = {}
    for doc_id, document in enumerate(data):
        score = 0
        token_counts = Counter(document['tokens'])
        for token in query_tokens:
            if token in token_counts:
                n = len([doc for doc in data if token in doc['tokens']])
                f = token_counts[token]
                idf = math.log((N - n + 0.5) / (n + 0.5) + 1)
                score += idf * (f * (k1 + 1)) / (f + k1 * (1 - b + b * (doc_lengths[doc_id] / avgdl)))
        results[doc_id] = score
    
    return sorted(results.keys(), key=lambda x: results[x], reverse=True)

if __name__ == "__main__":
    query_tokens = ["Attila", "Dorn", "Powerwolf"]
    print("Boolean Retrieval:", boolean_retrieval(query_tokens))
    print("Vector Space Model:", vector_space_model(query_tokens))
    print("BM25:", bm25(query_tokens))
