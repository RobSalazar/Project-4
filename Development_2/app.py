from flask import Flask, request, jsonify, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
from form import New_Astroid_Form
from predict import predictor
#Init
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = '1234'
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'astroid_db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#Init db
db = SQLAlchemy(app)

#Init ma
ma = Marshmallow(app)

#New Astroid Class/Model
class Astroids(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ad = db.Column(db.Float)
    q = db.Column(db.Float)
    a = db.Column(db.Float)
    e = db.Column(db.Float)
    dv = db.Column(db.Float)
    per = db.Column(db.Float)
    moid = db.Column(db.Float)
    diameter = db.Column(db.Float)

    def __init__(self, ad,q, a, e, dv, per, moid, diameter):
        self.ad = ad
        self.q = q
        self.a = a
        self.e = e
        self.dv = dv
        self.per = per
        self.moid = moid
        self.diameter = diameter

#New Astroid Schema
class NewAstroidSchema(ma.Schema):
    class Meta:                #Meta fields allowed to show
        fields = ('id','ad', 'q', 'a', 'e', 'dv', 'per', 'moid', 'diameter') 

#Init schema 
new_astroid_schema = NewAstroidSchema()
new_astroids_schema = NewAstroidSchema(many = True)

# #Enter new found Astroid
# @app.route('/New_Astroid', methods = ['POST'])
# def New_Astroid():
#     # return jsonify({"msg":"WORlD"})
#     ad = request.json['ad']
#     q = request.json['q']
#     a = request.json['a']
#     e = request.json['e']
#     dv = request.json['dv']
#     per = request.json['per']
#     moid = request.json['moid']
#     diameter = request.json['diameter']

#     new_astroid = Astroids(ad,q, a, e, dv, per, moid, diameter)
#     db.session.add(new_astroid)
#     db.session.commit()
#     return new_astroid_schema.jsonify(new_astroid)


# # Get All Astroids
# @app.route('/New_Astroids', methods=['GET'])
# def get_Astroids():
#     all_astroids = Astroids.query.all()
#     result = new_astroids_schema.dump(all_astroids)
#     return jsonify(result)

@app.route('/')
def home():
    
    return render_template('index.html')

@app.route('/Astroid_Form', methods=['GET', 'POST'])
def Astroid_Form():

    form = New_Astroid_Form()
    if form.validate_on_submit():
        flash(f'Your astriod has been created', 'success')
        return redirect(url_for('home'))
    return render_template('astroid_form.html', form = form)



#run serve 
if __name__ == '__main__':
    app.run(debug=True)