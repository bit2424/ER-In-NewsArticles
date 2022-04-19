import News
import Identificator
import Companies



def main():
    #testIdentifyandVerifyCompaniesInNews()
    testCompanyIdentification("NEVADA, Iowa (AP) — In 2008, this overwhelmingly white state was Barack Obamas unlikely launching pad to become the nations first Black president. Fourteen years later, Iowans arent showing a similar embrace for the woman running to become its first Black governor.")
    


def testNewsArticlesRetrieval():
    articles = News.getArticles('Politics', '','en','2022-04-13','2022-03-13',15)
    for article_content in articles:
        print(article_content['title']+' '+article_content['url'])


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
        for url in v['urls']:
            print(url)
        print()

def testIdentifyandVerifyCompaniesInNews():
    news = News.getArticles('Coffee', '','en','2022-04-13','2022-03-13',10)
    found_companies = Identificator.identify_companies_in_news(news)
    
    for k,v in found_companies.items():
        print("Company name: "+v['name'] + ' ', v['score'])
        print("\nPosible companies related: ")
        posible_companies = Companies.getCompanyInfo(v['name'])
        for comp in posible_companies['entities']:
            print(comp['identifier']['value'] + " ---- " + comp['short_description'])

        print('\n Found in next news: ')
        for url in v['urls']:
            print(url)
        print()

def testCompanyIdentification(entry):
    example = entry
    results = Identificator.identify_companies_in_text(example)
    print(results)

if __name__ == "__main__":
    main()