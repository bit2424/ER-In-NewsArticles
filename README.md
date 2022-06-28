## About the project:

We created a tool that allows you to identify companies in news articles that are related to a topic.

The project was developed to improve the process of bringing investor to the Colombian Pacific Region, identifying them in news articles and then trying to contact them to make new business partners. 

The system was built using python and specifically for the frontend the flask framework, the NLP models were integrated using the Huggingface API.

Based on a query the system consults news using NewsApi; from the selected news we filter the ones that are related to business, tech, and science, with DistilRoBERTa. Then, it identifies the entities mentioned in the news, using BERT-Large, and selects the ones related to organizations or businesses. Next, it collects possible real companies and information to contact them, associated to the entities in the previous step, with the Crunchbase API. At last, we classify the real companies into 62 categories with DistillBert.


### Execution process:

First you have to create a virtual enviroment in order to install the required libraries easier.
Here is a tutorial in how to do it https://docs.python.org/3/tutorial/venv.html

    my_env\Scripts\activate

If necesary you can execute the next command to allow the activation of the venv in windows:

    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass  

Any new library necesary to execute this process goes in requiremets.txt
Then you install it using:
    
    pip install -r requirements.txt

To execute the primary functionality of the app go to BackApp and play with the availible test methods

    py back/BackApp.py

Expected json request for backend:
{
    "query":"Coffee",
    "from-date":"2022-03-13",
    "to-date":"2022-05-15",
    "accepted-industries":[]
}

or filtering with industries:
{
    "query":"Coffee",
    "from-date":"2022-03-13",
    "to-date":"2022-05-15",
    "accepted-industries":["Restaurants"]
}

To execute the frontend execute:

    py front/front.py

Query view:
![imagen](https://user-images.githubusercontent.com/44851531/170073642-18f4495f-83ee-4d8d-ab23-b8bcb9624ee3.png)

Result view:
![imagen](https://user-images.githubusercontent.com/44851531/170073741-f0bca536-abe0-4659-ad43-175b29d2fb6c.png)


Possible Company Categories (casing is important):
* Advertising
* Aerospace & Defense
* Apparel Retail
* Apparel, Accessories & Luxury Goods
* Application Software
* Asset Management & Custody Banks
* Auto Parts & Equipment
* Biotechnology
* Building Products
* Casinos & Gaming
* Commodity Chemicals
* Communications Equipment
* Construction & Engineering
* Construction Machinery & Heavy Trucks
* Consumer Finance
* Data Processing & Outsourced Services
* Diversified Metals & Mining
* Diversified Support Services
* Electric Utilities
* Electrical Components & Equipment
* Electronic Equipment & Instruments
* Environmental & Facilities Services
* Gold
* Health Care Equipment
* Health Care Facilities
* Health Care Services
* Health Care Supplies
* Health Care Technology
* Homebuilding
* Hotels, Resorts & Cruise Lines
* Human Resource & Employment Services
* IT Consulting & Other Services
* Industrial Machinery
* Integrated Telecommunication Services
* Interactive Media & Services
* Internet & Direct Marketing Retail
* Internet Services & Infrastructure
* Investment Banking & Brokerage
* Leisure Products
* Life Sciences Tools & Services
* Movies & Entertainment
* Oil & Gas Equipment & Services
* Oil & Gas Exploration & Production
* Oil & Gas Refining & Marketing
* Oil & Gas Storage & Transportation
* Packaged Foods & Meats
* Personal Products
* Pharmaceuticals
* Property & Casualty Insurance
* Real Estate Operating Companies
* Regional Banks
* Research & Consulting Services
* Restaurants
* Semiconductors
* Specialty Chemicals
* Specialty Stores
* Steel
* Systems Software
* Technology Distributors
* Technology Hardware, Storage & Peripherals
* Thrifts & Mortgage Finance
* Trading Companies & Distributors
