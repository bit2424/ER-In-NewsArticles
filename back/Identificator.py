from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import News

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)

#Return a list of candidate companies that appear in a list of news articles 
#
def identify_companies_in_news(news):
  found_companies = {}
  nid = 0
  for n in news:
    #print(n)
    content =  n['description'] + '.' + n['content']
  
    #print(n['title'] + ': ' + n['description'])
    #proper_names = preprocess_article(content)
    ner_results = nlp(content)
    curr_company = ''
    for entity in ner_results:
      if 'ORG' in entity['entity']:
        if 'B' in entity['entity'] and "##" not in entity['word']:
          if curr_company != '' :
            if curr_company not in found_companies:
              #Here we could check if you can find the company
              found_companies[curr_company] = {'name': curr_company,'score': entity['score'],'description': "", 'newsid': [nid]}
              nid+=1
            else:
              if nid not in found_companies[curr_company]['newsid']:
                found_companies[curr_company]['newsid'].append(nid)

              found_companies[curr_company]['score'] = max(found_companies[curr_company]['score'] , entity['score'])

            #print("Complete: "+curr_company)
          curr_company = entity['word']
        else:
          if "##" in entity['word']:
            curr_company += entity['word'].replace("##", "")
          else:
            curr_company += " "+entity['word']
        
        #print(entity['entity']+" "+entity['word'])
  last_entity = ner_results[len(ner_results)-1]
  nid=-1
  if curr_company not in found_companies:
    found_companies[curr_company] = {'name': curr_company, 'score': last_entity['score'], 'newsid': [nid]}
  else:
    if nid not in found_companies[curr_company]['newsid']:
      found_companies[curr_company]['newsid'].append(nid)
    found_companies[curr_company]['score'] = max(found_companies[curr_company]['score'] , last_entity['score'])
  
  not_fitted_elements = []
  for k,v in found_companies.items():
      if(v['score']<0.75):
        not_fitted_elements.append(k)
        print(v['name'] + ': ', v['score'])

  for k in not_fitted_elements:
    del found_companies[k]

  return found_companies

def identify_companies_in_text(n):
  found_companies = {}
  #print(n)
  #print(n['title'] + ': ' + n['description'])
  #proper_names = preprocess_article(content)
  ner_results = nlp(n)
  curr_company = ''
  for entity in ner_results:
    if 'ORG' in entity['entity']:
      if 'B' in entity['entity'] and "##" not in entity['word']:
        if curr_company != '' :
          if curr_company not in found_companies:
            found_companies[curr_company] = {'name': curr_company,'score': entity['score']}
          else:
            found_companies[curr_company]['score'] = max(found_companies[curr_company]['score'] , entity['score'])

          #print("Complete: "+curr_company)
        curr_company = entity['word']
      else:
        if "##" in entity['word']:
          curr_company += entity['word'].replace("##", "")
        else:
          curr_company += " "+entity['word']
        
      #print(entity['entity']+" "+entity['word'])

  return found_companies

