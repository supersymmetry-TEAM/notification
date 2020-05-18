from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/contributer')
def aitest():
    return render_template('contributer.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Privacy')
def Pri():
    return render_template('Privacy.html')

if __name__== "__main__":
    app.run(host= '0.0.0.0',port ='5000')
    #app.run(debug=True)




    