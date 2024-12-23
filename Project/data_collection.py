import requests
from bs4 import BeautifulSoup
import json

def collect_data():
    # Define the topics to crawl related to Metal Music
    topics = [
        "Heavy_metal_music",
        "Powerwolf",
        "Thrash_metal",
        "Death_metal",
        "Black_metal",
        "Power_metal",
        "Metallica",
        "Iron_Maiden",
        "Black_Sabbath",
        "Slayer",
        "Megadeth",
        "Origins_of_heavy_metal",
        "New_Wave_of_British_Heavy_Metal",
        "Master_of_Puppets",
        "The_Number_of_the_Beast",
        "Paranoid_(album)",
        "Ozzy_Osbourne",
        "James_Hetfield",
        "Bruce_Dickinson",
        "Lemmy"
    ]
    
    base_url = "https://en.wikipedia.org/wiki/"
    documents = []
    
    for topic in topics:
        url = base_url + topic
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract text
        paragraphs = soup.find_all('p')
        document = "\n".join([para.text for para in paragraphs])
        documents.append({"url": url, "content": document})
    
    # Save to JSON
    with open('data.json', 'w') as f:
        json.dump(documents, f)

if __name__ == "__main__":
    collect_data()
