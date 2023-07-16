from flask import Flask,render_template
app1 = Flask(__name__)
@app1.route("/") 
def index():
    return  render_template('input.html')
if __name__ == "__main__": 
    app1.run(debug = True)
