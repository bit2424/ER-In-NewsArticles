import News
import Identificator
import Companies
import Clasificator



def main():
    testIdentifyandVerifyCompaniesInNews()
    #testCompanyIdentification("NEVADA Iowa AP In 2008, this overwhelmingly white state was Barack Obamas unlikely launching pad to become the nations first Black president. Fourteen years later, Iowans arent showing a similar embrace for the woman running to become its first Black governor.")
    #testNewsClasification()

def getCompanieOpts(query):
    results = {}
    return results

def testNewsArticlesRetrieval():
    articles = News.getArticles('Politics', '','en','2022-04-13','2022-03-13',15)
    for article_content in articles:
        print(article_content['title']+' '+article_content['newsid'])


def testCompanyInfoRetrieval():
    data = Companies.getCompanyInfo('Ford')
    #data = Companies.getCompanyInfo('C News Image')
    
    print(data['entities'][0].keys())

    print(data['entities'][0]['identifier'].keys())

    for comp in data['entities']:
        print(comp['identifier']['value'] + " ---- " + comp['short_description'])


def testCompaniesRetrieval():
    data = Companies.getEuropeBestCompanies()
    
    print(data['entities'][0].keys())

    print(data['entities'][0]['properties'].keys())

    for comp in data['entities']:
        print(comp['properties']['identifier']['value']+ " ---- " + comp['properties']['short_description'])

def testIdentifyCompaniesInNews():
    news = News.getArticles('Gaming', '','en','2022-04-13','2022-03-13',50)
    found_companies = Identificator.identify_companies_in_news(news)
    for k,v in found_companies.items():
        print(v['name'] + ': ' + v['score'])
        print('Found in')
        for newsid in v['newsid']:
            print(newsid)
        print()

def testIdentifyandVerifyCompaniesInNews():
    news = News.getArticles('video games', '','en','2022-04-19','2022-03-13',20)
    Clasificator.addNewsClass(news)
    found_companies = Identificator.identify_companies_in_news(news)
    
    result = {}
    #threshold = 0.7

    for k,v in found_companies.items():    
        #We have to check the companies are found in news relaeted to business
        isBusiness = False
        relevant_news = []
        print('\n Found in next news: ')
        for newsid in v['newsid']:
            for c in news[newsid]['class']:
                if(c['label'] == 'Business'):
                    print(news[newsid]['url'])
                    print(c['label']+" ",c['score'])
                    relevant_news.append(news[newsid])
                    isBusiness = True
        print()

    if(isBusiness):
        
        for k,v in found_companies.items():
            
            posible_companies = Companies.getCompanyInfo(v['name'])


            if(len(posible_companies)>0):
                print("Company name: "+v['name'] + ' ', v['score'])
                print("\nPosible companies related: ")
                result[v['name']] = {}
                result[v['name']]['confidence'] =  v['score']
                result[v['name']]['news'] = relevant_news
                result[v['name']]['compainies_info'] = {}
                Clasificator.addCompaniesClass(posible_companies)

                for comp in posible_companies['entities']:
                    #We have to check the companies being selected are related to business topic
                    for c in comp['class']:
                        if(c['label']=='Business'):
                            print("tag: "+c['label']+" ",c['score'])
                            print(comp['identifier']['value'] + " ---- " + comp['short_description'])
                            result[v['name']]['compainies_info'][comp['identifier']['value']] = {}
                            result[v['name']]['compainies_info'][comp['identifier']['value']]['short_description'] = comp['short_description']
                            result[v['name']]['compainies_info'][comp['identifier']['value']]['name'] = comp['identifier']['value']
                            result[v['name']]['compainies_info'][comp['identifier']['value']]['score'] = c['score']

    return result
            

def testNewsClasification():
    news = News.getArticles('Coffee', '','en','2022-04-13','2022-03-13',10)
    Clasificator.addNewsClass(news)
    for n in news:
        print(n['title'])
        for c in n['class']:
            print(c['label']+" ",c['score'])


def testCompanyIdentification(entry):
    example = entry
    results = Identificator.identify_companies_in_text(example)
    print(results)

if __name__ == "__main__":
    main()