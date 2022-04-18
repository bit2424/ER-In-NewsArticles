from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        query = request.form['query']
        print("#################",query)

    return render_template("index.html")



if __name__ == "__main__":
	app.run()
