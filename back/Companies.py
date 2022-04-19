import requests
import json

#Search for a particular companie
#A data['entities'] has keys ['facet_ids', 'identifier', 'short_description']
#If you get the identifier for a particular entitie it has keys ['uuid', 'value', 'image_id', 'permalink', 'entity_def_id']
#In general you are intereseted in the [value] of the [identifier] for a particular particular entity
#
#For a particular query there exist various candidates that can be suitable as entities
def getCompanyInfo(company):
  url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/autocompletes"

  querystring = {"query":company}

  headers = {
      'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
      'x-rapidapi-key': "1967cc7724mshc089354d6196768p1f0b53jsnade70c00a4a0"
  }

  response = requests.request("GET", url, headers=headers, params=querystring)

  #print(response.text)
  
  data = {}

  if(response != None):
    data = json.loads(response.text)

  #print(data.keys())
  
  return data


#Search for a group of companies from Europe, I dont know yet how to ge companies from other places
#
#A data['entities'] has keys ['uuid', 'properties']
#If you get the properties for a particular entity it has keys ['identifier', 'short_description', 'rank_org', 'location_identifiers']
#In general you are intereseted in the [properties] of data['entities'] for a particular particular entity
#
#
def getEuropeBestCompanies():
  url = "https://crunchbase-crunchbase-v1.p.rapidapi.com/searches/organizations"

  #We can map the location identifiers that we get of the companies and try to get companies from different places

  payload = "{\r\n    \"field_ids\": [\r\n        \"identifier\",\r\n        \"location_identifiers\",\r\n        \"short_description\",\r\n        \"rank_org\"\r\n    ],\r\n    \"limit\": 50,\r\n    \"order\": [\r\n        {\r\n            \"field_id\": \"rank_org\",\r\n            \"sort\": \"asc\"\r\n        }\r\n    ],\r\n    \"query\": [\r\n        {\r\n            \"field_id\": \"location_identifiers\",\r\n            \"operator_id\": \"includes\",\r\n            \"type\": \"predicate\",\r\n            \"values\": [\r\n                \"6106f5dc-823e-5da8-40d7-51612c0b2c4e\"\r\n            ]\r\n        },\r\n        {\r\n            \"field_id\": \"facet_ids\",\r\n            \"operator_id\": \"includes\",\r\n            \"type\": \"predicate\",\r\n            \"values\": [\r\n                \"company\"\r\n            ]\r\n        }\r\n    ]\r\n}"
  headers = {
      'content-type': "application/json",
      'x-rapidapi-host': "crunchbase-crunchbase-v1.p.rapidapi.com",
      'x-rapidapi-key': "1967cc7724mshc089354d6196768p1f0b53jsnade70c00a4a0"
  }

  response = requests.request("POST", url, data=payload, headers=headers)

  data = json.loads(response.text)

  #print(data.keys())
  
  return data