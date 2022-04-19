import News
import Identificator
import Companies



def main():
    testIdentifyCompaniesInNews()


def testNewsArticlesRetrieval():
    articles = News.getArticles('Politics', '','en','2022-04-13','2022-03-13',15)
    for article_content in articles:
        print(article_content['title']+' '+article_content['url'])


def testCompanyInfoRetrieval():
    data = Companies.getCompanyInfo('Ford')
    
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
        print(v['name'] + ': ' + v['description'])
        print('Found in')
        for url in v['urls']:
            print(url)
        print()

def testIdentifyandVerifyCompaniesInNews():
    news = News.getArticles('Gaming', '','en','2022-04-13','2022-03-13',50)
    found_companies = Identificator.identify_companies_in_news(news)
    for k,v in found_companies.items():
        print(v['name'] + ': ' + v['description'])
        print('Found in')
        for url in v['urls']:
            print(url)
        print()

if __name__ == "__main__":
    main()