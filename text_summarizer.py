from transformers import pipeline

# Load the summarization pipeline
print("📦 Loading model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("🚀 Script is running")

    input_text = """
    Artificial Intelligence (AI) is transforming industries by automating tasks,
    analyzing large amounts of data, and improving decision-making. From healthcare
    to finance, AI applications are providing better efficiency and accuracy.
    In the healthcare sector, AI can assist in diagnosing diseases, managing patient records,
    and even predicting health outcomes. Financial institutions use AI for fraud detection,
    risk assessment, and customer service automation. Despite its benefits, AI also poses challenges
    such as data privacy concerns, job displacement, and ethical dilemmas. It is crucial for companies
    and governments to implement responsible AI practices to ensure transparency, fairness, and accountability.
    As the field continues to grow, interdisciplinary collaboration will be key in harnessing the full
    potential of AI for societal good.
    """

    print("Original Text:\n", input_text)
    print("\nSummarized Text:\n", summarize_text(input_text))
