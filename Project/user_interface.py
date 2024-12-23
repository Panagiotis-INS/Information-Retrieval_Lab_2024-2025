from query_processing import search

def user_interface():
    query = input("Enter your search query: ")
    print("Select retrieval method:")
    print("1. Boolean Retrieval")
    print("2. Vector Space Model (VSM)")
    print("3. Probabilistic Retrieval (BM25)")
    method_choice = input("Enter the number corresponding to your choice: ")

    if method_choice == "1":
        method = "boolean"
    elif method_choice == "2":
        method = "vsm"
    elif method_choice == "3":
        method = "bm25"
    else:
        print("Invalid choice. Defaulting to Boolean Retrieval.")
        method = "boolean"

    results = search(query, method)
    print(f"Search Results for '{query}' using {method} method:")
    for result in results:
        print(result)

if __name__ == "__main__":
    user_interface()
