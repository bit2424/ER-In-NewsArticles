from asyncore import compact_traceback
from ensurepip import bootstrap
from urllib.parse import urlencode
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, DateField, SelectMultipleField,SubmitField)
from wtforms.validators import InputRequired, Length


import os
SECRET_KEY = os.urandom(32)

import requests

app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY

context = {}

company_categories = [
('1','Advertising'),
('2','Aerospace & Defense'),
('3','Apparel Retail'),
('4','Apparel, Accessories & Luxury Goods'),   
('5','Application Software'),
('6','Asset Management & Custody Banks'),      
('7','Auto Parts & Equipment'),
('8','Biotechnology'),
('9','Building Products'),
('10','Casinos & Gaming'),
('11','Commodity Chemicals'),
('12','Communications Equipment'),
('13','Construction & Engineering'),
('14','Construction Machinery & Heavy Trucks'),
('15','Consumer Finance'),
('16','Data Processing & Outsourced Services'),
('17','Diversified Metals & Mining'),
('18','Diversified Support Services'),
('19','Electric Utilities'),
('20','Electrical Components & Equipment'),
('21','Electronic Equipment & Instruments'),
('22','Environmental & Facilities Services'),
('23','Gold'),
('24','Health Care Equipment'),
('25','Health Care Facilities'),
('26','Health Care Services'),
('27','Health Care Supplies'),
('28','Health Care Technology'),
('29','Homebuilding'),
('30','Hotels, Resorts & Cruise Lines'),
('31','Human Resource & Employment Services'),
('32','IT Consulting & Other Services'),
('33','Industrial Machinery'),
('34','Integrated Telecommunication Services'),
('35','Interactive Media & Services'),
('36','Internet & Direct Marketing Retail'),
('37','Internet Services & Infrastructure'),
('38','Investment Banking & Brokerage'),
('39','Leisure Products'),
('40','Life Sciences Tools & Services'),
('41','Movies & Entertainment'),
('42','Oil & Gas Equipment & Services'),
('43','Oil & Gas Exploration & Production'),
('44','Oil & Gas Refining & Marketing'),
('45','Oil & Gas Storage & Transportation'),
('46','Packaged Foods & Meats'),
('47','Personal Products'),
('48','Pharmaceuticals'),
('49','Property & Casualty Insurance'),
('50','Real Estate Operating Companies'),
('51','Regional Banks'),
('52','Research & Consulting Services'),
('53','Restaurants'),
('54','Semiconductors'),
('55','Specialty Chemicals'),
('56','Specialty Stores'),
('57','Steel'),
('58','Systems Software'),
('59','Technology Distributors'),
('60','Technology Hardware, Storage & Peripherals'),
('61','Thrifts & Mortgage Finance'),
('62','Trading Companies & Distributors'),
]

class QueryForm(FlaskForm):
    query = TextAreaField('Digit the descritption for the news you want to obtain:',
                                validators=[InputRequired(),
                                            Length(min=2,max=200)])

    #Parece que este es el formato correcto
    date_from = DateField('Select the start date for the search:', validators=[InputRequired()])

    date_to = DateField('Select the end date for the search:',validators=[InputRequired()])
    
    industries = SelectMultipleField('Select the categories of the companies you want to see in the results:',choices = company_categories, default = ['1', '63'],)

    submit = SubmitField()

@app.route("/table", methods=["GET", "POST"])
def generateTables():
    if request.method == 'POST':
        form_out = request.form
        #print(form_out)
        # selected_industries = []
        # for idx in form_out.getlist('industries'):
        #     selected_industries.append(company_categories[int(idx)-1][1] )
        # #print(selected_industries)
        # date_from = form_out['date_from']
        # date_to = form_out['date_to']
        # query = form_out['query']
        # URL = "http://localhost:8080/find-companies"
        # data = {'query':query,
        #            'from-date':date_from,
        #            'to-date':date_to,
        #            'accepted-industries':selected_industries
        # }
        # print()
        # r = requests.get(url = URL, json=data)
        # data = r.json()
        # context['elems'] = data
    
    context['Title'] = "Results for the query"
    return render_template("bootstrap_table.html",**context)

@app.route('/', methods=["GET", "POST"])
def index():
    #companiesOpt = back.getCompanieOpts()
    form = QueryForm()
    context['form'] = form
    print(form)
    context['Title'] = "Make a Query"

    if form.validate_on_submit():
        flash('The query is being preformed')
        return redirect('bootstrap_table.html',**context)

    return render_template('index.html',**context)

@app.before_first_request
def initialize():
    context['elems'] = ["Esto", "es", "una", "prueba"]
    selected_industries = []
    for idx in company_categories:
        selected_industries.append(idx[1] )
    #print(selected_industries)
    URL = "http://localhost:8080/find-companies"
    data = {'query':'food',
                'from-date':'2022-05-15',
                'to-date':'2022-04-26',
                'accepted-industries':selected_industries
    }
    #print()
    r = requests.get(url = URL, json=data)
    data = r.json()
    #print(data,"\n")
    context['elems'] = data
    #print(data[0]['candidates'])
    #context['queryResult'] = back.testIdentifyandVerifyCompaniesInNews()

if __name__ == "__main__":
    app.run(debug=True)
