from flask import Flask, request, render_template
import os
from think import thinker

#Init
app = Flask(__name__)

@app.route('/')
def Astroid_Form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def Astroid_Form_post():
    variable = request.form['variable']
    return thinker(variable)



#run serve 
if __name__ == '__main__':
    app.run(debug=True)