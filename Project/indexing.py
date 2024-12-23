import json
from collections import defaultdict

def create_index():
    with open('preprocessed_data.json', 'r') as f:
        data = json.load(f)
    
    inverted_index = defaultdict(list)
    
    for doc_id, document in enumerate(data):
        for token in document['tokens']:
            inverted_index[token].append(doc_id)
    
    # Save index
    with open('index.json', 'w') as f:
        json.dump(inverted_index, f)

if __name__ == "__main__":
    create_index()
