import News
import Identificator
import Companies
import Clasificator
import json
from flask import Flask, request

app = Flask(__name__)
MAX_RELATED_COMPANIES = 3

@app.route('/find-companies')
def findCompaniesInNews():

    request_data = request.get_json()
    query = request_data['query']
    from_date = request_data['from-date']
    to_date = request_data['to-date']
    accepted_industries = request_data['accepted-industries']

    news = News.getArticles(query, '','en',to_date,from_date,20)
    # We only care about Sci/Tech or Business news
    Clasificator.addNewsClass(news)
    accepted_news_labels = {'Business','Sci/Tech'}
    news = [n for n in news if n['class'][0]['label'] in accepted_news_labels]

    found_companies = Identificator.identify_companies_in_news(news)

    result = []
    for company,news in found_companies.items():
        current = {"name": company, "news": news}
        posible_companies = Companies.getCompanyInfo(company)
        candidates = []
        if(len(posible_companies)>0):
            cnt = MAX_RELATED_COMPANIES
            for comp in posible_companies['entities']:
                if cnt == 0:
                    break
                desc = comp['short_description']
                ind = Companies.getCompanyIndustry(desc)
                print(comp['identifier']['value'] + " ---- " + desc + " ---- " + ind)
                if len(accepted_industries)==0 or ind in accepted_industries:
                    social_networks = Companies.getCompanySocialNetworks(comp['identifier']['uuid'])
                    curr_candidate = {"name": comp['identifier']['value'], "description": desc, "industry": ind}
                    curr_candidate.update(social_networks)
                    candidates.append(curr_candidate)
                    cnt -= 1

        current['candidates'] = candidates
        result.append(current)
    return json.dumps(result)

if __name__ == "__main__":
    app.run(debug=True, port=8080)