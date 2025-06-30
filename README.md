# text-summarizer

*COMPANY NAME*: CODTECH IT SOLUTIONS

*NAME*:TEKI RAJA

*INTERN ID*:CT06DM638

*DOMAIN*:Artificial intelligence

*DURATION*: 6 weeks 

*MENTOR*:Neela Santhosh Kumar

##DESCERPTION##

🧱 1. Loading the Summarization Model

from transformers import pipeline

print("📦 Loading model…")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
pipeline("summarization", …): Initializes an abstraction that handles tokenization, model inference, and output formatting for summarization tasks. 

Model: You’re using the pre‑trained facebook/bart-large-cnn checkpoint—an encoder-decoder transformer fine‑tuned on the CNN/DailyMail dataset for abstractive summarization. 

✂️ 2. Summary Function
def summarize_text(text, max_length=130, min_length=30):
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
Parameters:

max_length / min_length: Control summary token count.

do_sample=False: Uses deterministic beam search for consistent results. 


Output: A list of results—taking index [0] to fetch the first summary result. It then returns the summary text string.

🚀 3. Running the Script

if __name__ == "__main__":
    print("🚀 Script is running")
    input_text = """…long AI paragraph…"""
    print("Original Text:\n", input_text)
    print("\nSummarized Text:\n", summarize_text(input_text))
When run directly, it will:

Print a “script is running” notice.

Show the original input text.

Generate and print the concise summary via summarize_text

## steps for executions##
1. open vs code or jupter notebook.
2.open a new folder in desired location(where user want to save the file).
3.open a text file.
4. copy the code in git these github repository or type it.
5. name the file as text_summarizer.py .
6. for run the script user have download some depencies or libraries like (hugging face).
7. for downloading depencies go terminal in vs code.
8. then run these command pip install transformers torch.
9. it will download the file it takes nearly (1.6)gb data for first time.
10. then run the final command the execute the code is python text_summarizer.py
11. it will shows the output like this.
