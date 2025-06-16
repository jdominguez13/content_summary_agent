from transformers import pipeline

def summarize_article(content, url=None):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(content, max_length=80, min_length=30, do_sample=False)
    summary_text = summary[0]['summary_text'].strip()
    if url:
        summary_text += f"\nRead more: {url}"
    return summary_text

if __name__ == '__main__':
    test_content = "OpenAI's new tools are helping businesses automate tasks and increase revenue..."
    test_url = "https://example.com/full-article"
    print(summarize_article(test_content, test_url)) 


# from transformers import pipeline

# def summarize_article(content):
#     summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
#     summary = summarizer(content, max_length=100, min_length=30, do_sample=False)
#     return summary[0]['summary_text']

# if __name__ == '__main__':
#     test_content = "OpenAI's new tools are helping businesses automate tasks and increase revenue..."
#     print(summarize_article(test_content)) 