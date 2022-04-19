import News
import Identificator
import Companies
import Clasificator



def main():
    testIdentifyandVerifyCompaniesInNews()
    #testCompanyIdentification("NEVADA Iowa AP In 2008, this overwhelmingly white state was Barack Obamas unlikely launching pad to become the nations first Black president. Fourteen years later, Iowans arent showing a similar embrace for the woman running to become its first Black governor.")
    #testNewsClasification()


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
    news = News.getArticles('Cars', '','en','2022-04-13','2022-03-13',10)
    Clasificator.addNewsClass(news)
    found_companies = Identificator.identify_companies_in_news(news)
    
    for k,v in found_companies.items():
        print("Company name: "+v['name'] + ' ', v['score'])
        print("\nPosible companies related: ")
        posible_companies = Companies.getCompanyInfo(v['name'])
        Clasificator.addCompaniesClass(posible_companies)
        for comp in posible_companies['entities']:
            print(comp['identifier']['value'] + " ---- " + comp['short_description'])
            for c in comp['class']:
                print("tag: "+c['label']+" ",c['score'])

        print('\n Found in next news: ')
        for newsid in v['newsid']:
            print(news[newsid]['url'])
            for c in news[newsid]['class']:
                print(c['label']+" ",c['score'])
        print()

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