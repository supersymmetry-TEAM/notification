from flask import Flask, render_template, request, redirect, send_file
app = Flask(__name__)

@app.route('/1')
def get_image_1():
    name = "./source/1.png"
    return send_file(name)
@app.route('/2')
def get_image_2():
    name = "./source/2.png"
    return send_file(name)
@app.route('/blog')
def index():
    return render_template('index.html')
if __name__== "__main__":
    app.run(host= '0.0.0.0',port ='5000')
    #app.run(debug=True)




    
