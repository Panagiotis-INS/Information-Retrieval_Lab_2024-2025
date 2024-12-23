def precision_at_k(relevant_documents, retrieved_documents, k):
    retrieved_at_k = retrieved_documents[:k]
    relevant_retrieved_at_k = [doc for doc in retrieved_at_k if doc in relevant_documents]
    return len(relevant_retrieved_at_k) / k

def recall_at_k(relevant_documents, retrieved_documents, k):
    retrieved_at_k = retrieved_documents[:k]
    relevant_retrieved_at_k = [doc for doc in retrieved_at_k if doc in relevant_documents]
    return len(relevant_retrieved_at_k) / len(relevant_documents)

def f1_score_at_k(relevant_documents, retrieved_documents, k):
    precision = precision_at_k(relevant_documents, retrieved_documents, k)
    recall = recall_at_k(relevant_documents, retrieved_documents, k)
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

def average_precision(relevant_documents, retrieved_documents):
    ap_sum = 0
    relevant_count = 0
    for i, doc in enumerate(retrieved_documents):
        if doc in relevant_documents:
            relevant_count += 1
            ap_sum += relevant_count / (i + 1)
    return ap_sum / len(relevant_documents)

def mean_average_precision(relevant_documents_list, retrieved_documents_list):
    ap_sum = 0
    for relevant_documents, retrieved_documents in zip(relevant_documents_list, retrieved_documents_list):
        ap_sum += average_precision(relevant_documents, retrieved_documents)
    return ap_sum / len(relevant_documents_list)

def evaluate(relevant_documents_list, retrieved_documents_list):
    precision_scores = []
    recall_scores = []
    f1_scores = []
    map_score = mean_average_precision(relevant_documents_list, retrieved_documents_list)
    
    for relevant_documents, retrieved_documents in zip(relevant_documents_list, retrieved_documents_list):
        k = len(retrieved_documents)
        precision_scores.append(precision_at_k(relevant_documents, retrieved_documents, k))
        recall_scores.append(recall_at_k(relevant_documents, retrieved_documents, k))
        f1_scores.append(f1_score_at_k(relevant_documents, retrieved_documents, k))
    
    avg_precision = sum(precision_scores) / len(precision_scores)
    avg_recall = sum(recall_scores) / len(recall_scores)
    avg_f1 = sum(f1_scores) / len(f1_scores)
    
    print(f"Average Precision: {avg_precision:.4f}")
    print(f"Average Recall: {avg_recall:.4f}")
    print(f"Average F1-Score: {avg_f1:.4f}")
    print(f"Mean Average Precision (MAP): {map_score:.4f}")

if __name__ == "__main__":
    # Sample data for testing
    relevant_documents_list = [
        ["doc1", "doc2", "doc3"],
        ["doc1", "doc4", "doc5"]
    ]
    
    retrieved_documents_list = [
        ["doc1", "doc2", "doc4", "doc5"],
        ["doc1", "doc2", "doc3", "doc4"]
    ]
    
    evaluate(relevant_documents_list, retrieved_documents_list)
