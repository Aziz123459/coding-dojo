from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = 'secret'  

@app.route('/')
def index():
    if 'visit_counter' not in session:
        session['visit_counter'] = 1
    else:
        session['visit_counter'] += 1
    return render_template('index.html')

@app.route('/clear')
def clear():
    session.clear() 
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
