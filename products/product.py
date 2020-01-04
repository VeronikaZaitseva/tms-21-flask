from app import db


class Product(db.Model):
    id = db.Column('product_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer(20))
    amount = db.Column(db.Integer(20))
    comment = db.Column(db.String(200))

    def __init__(self, name, price, amount, comment):
        self.name = name
        self.price = price
        self.amount = amount
        self.comment = comment

    def __repr__(self):
        return "<Product id: {}, name: {}, price: {}, amount: {}, comment: {}".format(self.id, self.name, self.price,
                                                                                      self.amount, self.comment)