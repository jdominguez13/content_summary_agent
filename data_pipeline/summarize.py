from transformers import pipeline

def summarize_article(content):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(content, max_length=50, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == '__main__':
    test_content = "OpenAI's new tools are helping businesses automate tasks and increase revenue..."
    print(summarize_article(test_content)) 