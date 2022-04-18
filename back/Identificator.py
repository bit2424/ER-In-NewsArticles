from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import News

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "My name is Wolfgang and I live in Berlin"

ner_results = nlp(example)
print(ner_results)

def identify_companies_in_news_by_query(query, from_date, to_date, language='en', how_many_news=10):
  news = News.get_raw_news(query, from_date, to_date, language, how_many_news)
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
              companies_temp[curr_company] = {'name': curr_company, 'description': "", 'urls': [url]}
            else:
              if url not in companies_temp[curr_company]['urls']:
                companies_temp[curr_company]['urls'].append(url)

            print("Complete: "+curr_company)
          curr_company = entity['word']
        else:
          if "##" in entity['word']:
            curr_company += entity['word'].replace("##", "")
          else:
            curr_company += " "+entity['word']
        
        #print(entity['entity']+" "+entity['word'])
    
  if curr_company not in companies_temp:
    #Here we could check if you can find the company
    companies_temp[curr_company] = {'name': curr_company, 'description': '', 'urls': [url]}
  else:
    if url not in companies_temp[curr_company]['urls']:
      companies_temp[curr_company]['urls'].append(url)
    
  return companies_temp

query = 'gaming'
from_date = '2022-04-01'
to_date = '2022-03-01'
language = 'en'
how_many_news = 50

found_companies = identify_companies_in_news_by_query(query, from_date, to_date, language, how_many_news)
#print(found_companies)
for k,v in found_companies.items():
  print(v['name'] + ': ' + v['description'])
  print('Found in')
  for url in v['urls']:
    print(url)
  print()