from flask import Flask, render_template, request 
#import pandas as pd
app2 = Flask(__name__)
@app2.route("/")
def index():
    return render_template('input.html')
@app2.route('/result', methods = ['POST', 'GET'])
def result():
    #pd.read_csv('')
    income = float(request.form.get('income'))
    nd = int(request.form.get('nd'))
    tax = (income - 10000 - 3000 * nd) * 0.2
    return render_template('result.html', tax = tax)
if __name__ == "__main__":
    app2.run(debug = True)  