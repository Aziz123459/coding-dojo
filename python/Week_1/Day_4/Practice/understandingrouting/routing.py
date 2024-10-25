from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "hello world"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def name(name):
    return "hi "+name
@app.route('/repeat/<int:number>/<name>')
def hello(number,name):
    return (name+" ") * number 
@app.errorhandler(404)
def page_not_found(e):
    return 'The value times needs to be an integer', 404





if __name__=="__main__": 
    app.run(debug=True) 