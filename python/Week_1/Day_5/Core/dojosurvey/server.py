from flask import Flask,render_template,session,redirect,request
app = Flask(__name__) 
app.secret_key='secret'   
@app.route('/')          
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('info.html')
@app.route('/submit',methods=['POST'])
def submit():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment']=request.form['comment']
    return redirect('/result')

if __name__=="__main__":    
    app.run(debug=True)    

