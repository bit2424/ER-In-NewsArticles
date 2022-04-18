from newsapi import NewsApiClient

searchDomains = 'npr.org,c-span.org,economist.com,apnews.com,bbc.com,techcrunch.com'

#The keys of the collection of articles are ['status', 'totalResults', 'articles'])
#The keys of one article are ['source', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content']
def getArticles(newsTopic,newsSources,newsLanguge, newsFromDate , newsTillDate, numbResults):
    # Init
    newsapi = NewsApiClient(api_key='43a1c14e338642f0a53f493c8814b7e5')

    # /v2/top-headlines
    #top_headlines = newsapi.get_top_headlines(  q=newsTopic, sources=newsSources, language=newsLanguge)

    # /v2/everything
    all_articles = newsapi.get_everything(q= newsTopic,
                                        sources= newsSources,
                                        domains= searchDomains,
                                        from_param= newsFromDate,
                                        to= newsTillDate,
                                        language= newsLanguge,
                                        sort_by='relevancy',
                                        page=1,
                                        page_size= numbResults)
    
    return all_articles['articles']


#This method updates the search domains based on a particular topic that allows us to get more relevant results
def updateSearchDomain(topic):
    if topic:
        searchDomains = ''
    

#for article in all_articles:
    #print(article)

# /v2/top-headlines/sources
#sources = newsapi.get_sources()
#print(sources)
