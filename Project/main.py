from data_collection import collect_data
from text_preprocessing import preprocess_text
from indexing import create_index
from user_interface import user_interface

def main():
    collect_data()
    preprocess_text()
    create_index()
    user_interface()

if __name__ == "__main__":
    main()
