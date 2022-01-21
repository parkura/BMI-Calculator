from flask import Flask,  render_template, request

import os

app = Flask(__name__)

app.secret_key = os.urandom(24)


@app.route('/')
@app.route('/input')
def register():
    return render_template("form.html")

@app.route('/form', methods=["GET","POST"])
def form():
        name = request.form.get("name")
        surname = request.form.get("surname")
        weight = float(request.form.get("weight"))
        height = float(request.form.get("height"))
        bmi = weight / (height/100)**2
        return render_template("database.html", name = name, surname=surname, weight=weight, height=height, bmi=bmi)



if __name__ == '__main__':
    app.run(debug=True)