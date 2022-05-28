from flask import Flask, render_template
app = Flask(__name__)

inputs = [{'Spectral Type':'input_1',
'Aphelion Distance':'input_2',
'Perihelion':'input_3',
'Semi-Major Axis':'input_4',
'Eccentricity':'input_5',
'Delta Velocity':'input_6',
'Period':'input_7',
'Minimum Orbit Intersection Distance':'input_8'}]

# Route to render index.html template
@app.route("/")
def index():
    return render_template('index.html', inputs=inputs)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)