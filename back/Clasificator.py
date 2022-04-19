from transformers import AutoTokenizer, AutoModelForSequenceClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("mrm8488/bert-mini-finetuned-age_news-classification")

model = AutoModelForSequenceClassification.from_pretrained("mrm8488/bert-mini-finetuned-age_news-classification")

nlp = pipeline("text-classification", model = model, tokenizer=tokenizer)

def clasifyText(text):
    class_results = nlp(text)
    return class_results

def addNewsClass(news):
    for n in news:
        content = n['title'] + ',' + n['description'] + ',' + n['content']
        pred_results = clasifyText(content)
        n['class'] = pred_results

def addCompaniesClass(posible_companies):
    for comp in posible_companies['entities']:
        pred_results = clasifyText(comp['short_description'])
        comp['class'] = pred_results