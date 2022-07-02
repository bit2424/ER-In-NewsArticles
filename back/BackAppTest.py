import News
import Identificator
import Companies
import Clasificator



def main():
    dataSetCreation()

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
        print(k + ': ' + v['score'])
        print('Found in')
        for newsid in v['newsid']:
            print(newsid)
        print()

def testIdentifyandVerifyCompaniesInNews():
    news = News.getArticles('Coffee', '','en','2022-05-15','2022-03-13',20)
    # We only care about Science and Technology or Business news
    Clasificator.addNewsClass(news)
    
    found_companies = Identificator.identify_companies_in_news(news)
    
    result = {}
    result['companies'] = {}

    for company,news in found_companies.items():
        print("Company name: "+company)
        print("\nPosible companies related: ")
        posible_companies = Companies.getCompanyInfo(company)

        result['companies'][company] = {}

        if(len(posible_companies)>0):
            cnt = 5
            for comp in posible_companies['entities']:
                desc = comp['short_description']
                ind = Companies.getCompanyIndustry(desc)
                print(comp['identifier']['value'] + " ---- " + desc + " ---- " + ind)
                if cnt == 0:
                    break
                cnt -= 1         


            print('\n Found in next news: ')
            for n in news:
                print(n['title']+" - "+n['url'])
            print()

def testNewsClasification():
    news = News.getArticles('Coffee', '','en','2022-05-15','2022-04-20',10)
    Clasificator.addNewsClass(news)
    for n in news:
        print(n['title'])
        for c in n['class']:
            print(c['label']+" ",c['score'])


def testCompanyIdentification(entry):
    example = entry
    results = Identificator.identify_companies_in_text(example)
    print(results)

def dataSetCreation():
    news = News.getArticles('Investment Banking & Brokerage', '','en','2022-07-01','2022-06-05',20,[])
    # Clasificator.addNewsClass(articles)
    # accepted_news_labels = {'Business','Sci/Tech'}
    # news = [n for n in articles if n['class'][0]['label'] in accepted_news_labels]

    with open('dataset.txt', 'a',encoding='utf-8') as f:
        for article_content in news:
            f.write(article_content['title'].replace(',',' ')+"\n")

if __name__ == "__main__":
    main()