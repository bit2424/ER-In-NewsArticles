from asyncore import compact_traceback
from ensurepip import bootstrap
from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,RadioField,SubmitField)
from wtforms.validators import InputRequired, Length

import sys
sys.path.insert(0, 'back')
import BackApp as back

import os
SECRET_KEY = os.urandom(32)



app = Flask(__name__)
Bootstrap(app)
app.config['SECRET_KEY'] = SECRET_KEY

context = {'Title':"lol"}

class QueryForm(FlaskForm):
    description = TextAreaField('Query',
                                validators=[InputRequired(),
                                            Length(min=2,max=200)])
    level = RadioField('Location',
                       choices=['Colombia', 'America Latina'],
                       validators=[InputRequired()])
    submit = SubmitField()

@app.route("/table", methods=["GET", "POST"])
def generateTables():
    if request.method == 'POST':
        context["elems"] = request.form
        print("#################",request.form)
    context['Title'] = "Resultados de la busqueda"
    return render_template("bootstrap_table.html",**context)

@app.route('/', methods=["GET", "POST"])
def index():
    #companiesOpt = back.getCompanieOpts()
    form = QueryForm()
    context['form'] = form
    context['Title'] = "REALIZA UNA BUSQUEDA"
    return render_template('index.html',**context)

@app.before_first_request
def initialize():
    context['elems'] = ["Esto", "es", "una", "prueba"]
    #context['queryResult'] = back.testIdentifyandVerifyCompaniesInNews()

if __name__ == "__main__":
    app.run(debug=True)
