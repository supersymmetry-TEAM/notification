from flask import Flask, render_template, request, redirect, send_file
app = Flask(__name__)

@app.route('/contributer')
def aitest():
    return render_template('contributer.html')

@app.route('/')
def index():
    return render_template('index.html')
# http://example.com/get_image?type=1
@app.route('/get_image')
def get_image():
    name = "./source/gi.png"
    return send_file(name)
@app.route('/Privacy')
def Pri():
    return render_template('Privacy.html')

if __name__== "__main__":
    app.run(host= '0.0.0.0',port ='5000')
    #app.run(debug=True)




    