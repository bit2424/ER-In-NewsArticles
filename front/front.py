from asyncore import compact_traceback
from flask import Flask, render_template, request, redirect, url_for
import sys
sys.path.insert(0, 'back')
import BackApp as back



app = Flask(__name__)

context = {'Title':"lol"}

@app.route("/test", methods=["GET", "POST"])
def testTemplates():
    if request.method == 'POST':
        query = request.form['query']
        print("#################",query)
    Title = "Test"
    return render_template("index.html",**context)

@app.route("/table", methods=["GET", "POST"])
def generateTables():
    if request.method == 'POST':
        query = request.form['topic']
        print("#################",query)
    context['Title'] = "Resultados de la busqueda"
    return render_template("bootstrap_table.html",**context)

@app.route('/')
def index():
    #companiesOpt = back.getCompanieOpts()
    context['Title'] = "REALIZA UNA BUSQUEDA"
    return render_template('index.html',**context)

""" @app.route('/')
def index():
    companiesOpt = back.getCompanieOpts()
    return render_template('bootstrap_table.html', title='Bootstrap Table',
                           results=companiesOpt) """


def createDummyResults():
    context['elems'] = ["Esto", "es", "una", "prueba"]
    

if __name__ == "__main__":
    createDummyResults()
    app.run(debug=True)
