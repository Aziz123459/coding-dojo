from flask import Flask, render_template
app=Flask(__name__)



@app.route('/play')
def box():
    return render_template('index.html')



@app.route('/play/<int:x>')
def x_box(x):
    return render_template('index1.html',x=x)



@app.route('/play/<int:x>/<col>')
def color(x,col):
    return render_template('index2.html',x=x,col=col)

if __name__=="__main__":
    app.run(debug=True)  