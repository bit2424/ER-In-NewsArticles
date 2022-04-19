from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import News

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

#Return a list of candidate companies that appear in a list of news articles 
#
#
def identify_companies_in_news(news):
  companies_temp = {}
  for n in news:
    #print(n)
    content = n['title'] + '.' + n['description'] + '.' + n['content']
    url = n['url']
    #print(n['title'] + ': ' + n['description'])
    #proper_names = preprocess_article(content)
    ner_results = nlp(content)
    curr_company = ''
    for entity in ner_results:
      if 'ORG' in entity['entity']:
        if 'B' in entity['entity'] and "##" not in entity['word']:
          if curr_company != '' :
            if curr_company not in companies_temp:
              #Here we could check if you can find the company
              companies_temp[curr_company] = {'name': curr_company,'score': entity['score'],'description': "", 'urls': [url]}
            else:
              if url not in companies_temp[curr_company]['urls']:
                companies_temp[curr_company]['urls'].append(url)
              companies_temp[curr_company]['score'] = max(companies_temp[curr_company]['score'] , entity['score'])

            #print("Complete: "+curr_company)
          curr_company = entity['word']
        else:
          if "##" in entity['word']:
            curr_company += entity['word'].replace("##", "")
          else:
            curr_company += " "+entity['word']
        
        #print(entity['entity']+" "+entity['word'])
  last_entity = ner_results[len(ner_results)-1]
  if curr_company not in companies_temp:
    companies_temp[curr_company] = {'name': curr_company, 'score': last_entity['score'], 'description': '', 'urls': [url]}
  else:
    if url not in companies_temp[curr_company]['urls']:
      companies_temp[curr_company]['urls'].append(url)
    companies_temp[curr_company]['score'] = max(companies_temp[curr_company]['score'] , last_entity['score'])
    
  return companies_temp

def identify_companies_in_text(n):
  companies_temp = {}
  #print(n)
  #print(n['title'] + ': ' + n['description'])
  #proper_names = preprocess_article(content)
  ner_results = nlp(n)
  curr_company = ''
  for entity in ner_results:
    if 'ORG' in entity['entity']:
      if 'B' in entity['entity'] and "##" not in entity['word']:
        if curr_company != '' :
          if curr_company not in companies_temp:
            #Here we could check if you can find the company
            companies_temp[curr_company] = {'name': curr_company,'score': entity['score']}
          else:
            companies_temp[curr_company]['score'] = max(companies_temp[curr_company]['score'] , entity['score'])

          #print("Complete: "+curr_company)
        curr_company = entity['word']
      else:
        if "##" in entity['word']:
          curr_company += entity['word'].replace("##", "")
        else:
          curr_company += " "+entity['word']
        
        #print(entity['entity']+" "+entity['word'])
    
  return companies_temp


example = "However, a small number, including Burger King and UK retailer Marks and Spencer (M&S), have been unable to do so because their stores are run by franchise partners under complex legal arrangements."
results = identify_companies_in_text(example)
print(results)