import json
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def preprocess_text():
    with open('data.json', 'r') as f:
        data = json.load(f)
    
    ps = PorterStemmer()
    stop_words = set(stopwords.words('english'))
    
    for document in data:
        text = document['content']
        
        # Tokenization
        tokens = word_tokenize(text)
        
        # Stop-word removal
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
        
        # Stemming
        stemmed_tokens = [ps.stem(word) for word in filtered_tokens]
        
        document['tokens'] = stemmed_tokens
    
    # Save preprocessed data
    with open('preprocessed_data.json', 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    preprocess_text()
