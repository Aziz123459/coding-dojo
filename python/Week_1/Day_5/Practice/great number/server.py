from flask import Flask, render_template, session, request,redirect
import random

app=Flask(__name__)
app.secret_key="secret_key"


@app.route('/')

def render():
    if 'numb' not in  session :
        session['numb']= random.randint(1,100)
    return render_template('index.html')

@app.route('/submit',methods=['POST'])

def submit():
    guess=int(request.form['number'])

    if guess < session['numb']:
        hint="To low!"
    elif (guess>session['numb']):
        hint="To high!"
    else:
        hint="Good job you got the right answer"
    return render_template('index.html',hint=hint)


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')
    





if __name__ == "__main__" :
    app.run(debug=True)