General flow
============

Based on a query the system consults news using NewsApi; from the selected news we filter the ones that are related to business, tech, and science, with DistilRoBERTa. Then, it identifies the entities mentioned in the news, using BERT-Large, and selects the ones related to organizations or businesses. Next, it collects possible real companies and information to contact them, associated to the entities in the previous step, with the Crunchbase API. At last, we classify the real companies into 62 categories with DistillBert.

Finding companies in news
-------------------------

To retrieve a list of companies and their contact information from specific news articles. The news articles that we use are related to business, tech, and science;
you can use the ``BackApp.findCompaniesInNews()`` function:

.. py:function:: BackApp.findCompaniesInNews()

   Returns a json string representing the list of companies with their respective contact information.

   :returns: The companies list.
   :rtype: str

Get news articles 
-----------------

To retrieve news articles, from a given query, from the newsAPI, the search domains in which the query will be made are: ``c-span.org,economist.com,apnews.com,bbc.com,techcrunch.com``.

You can use the ``News.getArticles()`` function:

.. py:function:: News.getArticles(newsTopic, newsSources, newsLanguge, newsFromDate , newsTillDate, numbResults)

   Returns a json string representing the list of news articles that were queried.

   :param newsTopic: The topic that wants to be queried
   :param newsSources: Specific sources to be queried from, for example bbc-news or cnn. If left empty it will query any news source.
   :param newsLanguge: The queried news must be in this specified language.
   :param newsFromDate: The minimum date news articles can have.
   :param newsTillDate: The maximum date news articles can have.
   :param numbResults: Maximum number of results.
   :returns: The news articles list.
   :rtype: str

Classify news articles
----------------------

To classify news articles, from a given list, we use DistilRoBERTa. Specifically, we use `mrm8488/distilroberta-finetuned-age_news-classification <https://huggingface.co/mrm8488/distilroberta-finetuned-age_news-classification>`_

You can use the ``Clasificator.addNewsClass()`` function:

.. py:function:: Clasificator.addNewsClass(news)

   This function parses the received news articles in the form:

   ``title``, ``description``, ``content``

   and then classifies this new string into an array of different categories which can be found in `Usage <usage.html>`__.

   The functions then proceeds to assign the categories into this specific news article object for it to be used.

   :param news: The list of news articles to be classified.

Identify companies in news
--------------------------

To identify companies in news articles we use BERT-Large. Specifically, we use `bert-large-NER <https://huggingface.co/dslim/bert-large-NER>`_

You can use the ``Identificator.identify_companies_in_news()`` function:

.. py:function:: Identificator.identify_companies_in_news(news)

   This function returns a map {string, list}, the string represents the company that was identified and the list lists the titles and urls of the news articles where said company was found.

   :param news: The list of news articles where companies are to be identified from.
   :returns: A map of the companies and the list of news articles where said companies where found
   :rtype: map
