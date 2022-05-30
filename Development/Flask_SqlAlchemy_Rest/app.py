from flask import Flask, render_template,request, url_for, flash, redirect
from pickle import FALSE
from re import A
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

#Init app
app = Flask(__name__)
app.config['SECRET_KEY'] = '8e645c7b3eebfa899c04f2e51ffbfd4079cf34e4a26a7a92'
basedir = os.path.abspath(os.path.dirname(__file__))
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = FALSE
#Init db 
db = SQLAlchemy(app)
#Init ma
ma = Marshmallow(app)
values = []


#Product Class/Model
class Product(db.Model):
    ad = db.Column(db.Float, primary_key=True)
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

#Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('ad', 'q', 'a', 'e', 'dv', 'per', 'moid', 'diameter')

#Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many= True)

# ...

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        ad = request.form['ad']
        q = request.form['q']
        a = request.form['a']
        e = request.form['e']
        dv = request.form['dv']
        per = request.form['per']
        moid = request.form['moid']
        diameter = request.form['diameter']

        values.append({'ad': ad, 'q': q,'a': a, 'e': e, 'dv': dv, 'per': per, 'moid': moid, 'diameter': diameter})
        return redirect(url_for('index'))

    return render_template('create.html')
#Create a Product
@app.route('/product', methods=['POST'])
def add_product():
        ad = request.json['ad']
        q = request.json['q']
        a = request.json['a']
        e = request.json['e']
        dv = request.json['dv']
        per = request.json['per']
        moid = request.json['moid']
        diameter = request.json['diameter']
        new_product = Product(ad,q, a, e, dv, per, moid, diameter)

        db.session.add(new_product)
        db.session.commit()

        return product_schema.jsonify(new_product)

#Get all products
@app.route('/product', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify(result.data)

@app.route("/")
def index():
    return render_template('index.html')
    
#Run Server
if __name__ =='__main__':
    app.run(debug=True)