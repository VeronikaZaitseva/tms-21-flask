from app import app, db
from flask import render_template, request
from products import Product


@app.route("/")
def link():
    return render_template("index.html")


@app.route("/products")
def products():
    products = Product.query.all()
    return render_template("show_all.html", products=products)


@app.route("/products", methods=["POST"])
def add():
    if request.method == 'POST':
        name = request.form["Name"]
        price = request.form["Price"]
        amount = request.form["Amount"]
        comment = request.form["Comment"]
        product = Product(name=name, price=price, amount=amount, comment=comment)
        db.session.add(product)
        db.session.commit()
    return products()


@app.route("/products/<product_id>")
def information(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    return render_template("product.html", product=product)


@app.route("/products/<product_id>")
def delete(product_id):
    product = Product.query.filter(Product.id == product_id).first()
    db.session.delete(product)
    db.session.commit()
    return "Done"


@app.route("/products/<product_id>", methods=["POST"])
def edit(product_id):
    if request.method == 'POST':
        product = Product.query.filter(Product.id == product_id).first()
        value_name = request.form["Value to edit"]
        new_value = request.form["New value"]
        setattr(product, value_name, new_value)
        db.session.add(product)
        db.session.commit()
    return "Done"


