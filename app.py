# Import dependancies
from flask import Flask, request, render_template
from think import thinker

# Initialize flask
app = Flask(__name__)


# Route to landing page
@app.route('/')
def Astroid_Form():
    return render_template('index.html')

# Route for form to post user input
@app.route('/', methods=['POST'])
def Astroid_Form_post():
    variable = request.form['variable']
    return thinker(variable)




if __name__ == '__main__':
    app.run(debug=True)