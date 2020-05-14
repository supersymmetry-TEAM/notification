from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/aitest')
def aitest():
    return render_template('ai_test.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__== "__main__":
    app.run(debug=True)




    