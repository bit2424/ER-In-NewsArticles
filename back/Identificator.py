from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import News

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-large-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-large-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

always_discard = {"The Associated Press","AP", "en Español", "The"}

#Return a list of candidate companies that appear in a list of news articles 
#
def identify_companies_in_news(news):
  found_companies = {}
  for n in news:
    news_source = n['source']['name']
    content =  n['title']+'. '+n['content']
    content = content.replace("\r\n", ' ')
    content = content.replace("\n", ' ')
    companies = identify_companies_in_text(content)
    companies.discard(news_source)
    for c in always_discard:
      companies.discard(c)

    for c in companies:
      if c not in found_companies:
        found_companies[c] = list()
      newsinfo = {'title': n['title'], 'description': n['description'], 'url': n['url']}
      found_companies[c].append(newsinfo)

  return found_companies

#Identifies the posible organizations that are find in a particular text
def identify_companies_in_text(n):
  found_companies = set()
  ner_results = nlp(n)
  curr_st = -1
  curr_end = -1
  for entity in ner_results:
    if 'ORG' in entity['entity']:
      if 'B' in entity['entity']: #Beginning of the entity
        if curr_st != -1 and not (curr_end < len(n) and n[curr_end].isalpha()):
          found_companies.add(n[curr_st:curr_end])
        curr_st = -1
        if '##' not in entity['word']: #We do stuff only if the token is not a subword
          curr_st = entity['start']
          curr_end = entity['end']
      else: #Is not the beginning of the entity
        if curr_st != -1:
          curr_end = entity['end']
    else:
      if curr_st != -1 and not (curr_end < len(n) and n[curr_end].isalpha()):
        found_companies.add(n[curr_st:curr_end])
      curr_st = -1
    
  if curr_st != -1 and not (curr_end < len(n) and n[curr_end].isalpha()):
    found_companies.add(n[curr_st:curr_end])
  return found_companies

