from flask import Flask, render_template, request, redirect, send_file
app = Flask(__name__)

@app.route('/')
def get_image():
    name = "./source/gi.png"
    return send_file(name)
@app.route('/blog')
def index():
    return render_template('index.html')
if __name__== "__main__":
    app.run(host= '0.0.0.0',port ='5000')
    #app.run(debug=True)




    