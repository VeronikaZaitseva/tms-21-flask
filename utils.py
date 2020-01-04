def is_product_valid(form):
    return not form['name'] or not form['price'] or not form['amount']
