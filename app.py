from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

@app.route('/ping', methods=['Get'])
def ping():
    return jsonify({'message': 'pong'})

@app.route('/products', methods=['Get'])
def getProducts():
    return jsonify({'products': products, 'message': 'products list'})

@app.route('/products/<string:product_name>', methods=['Get'])
def getProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if(len(productsFound)>0):
        return jsonify({'product': productsFound[0]})
    else:
        return jsonify({'message': 'product not found'})

@app.route('/products', methods=['POST'])
def addProducts():
    newProduct= {
        'name': request.json['name'],
        'price': request.json['price'],
        'quantity': request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({'message': 'product added', 'products': products})

@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name ]
    if (len(productFound)>0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            'message': 'product updated',
            'products': productFound[0]
        })
    else:
        return jsonify({'message': 'product not found'})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name ]
    if (len(productFound)>0):
        products.remove(productFound[0])
        return jsonify({
            'message': 'product deleted',
            'products': products
        })
    else:
        return jsonify({'message': 'product not found'})

@app.route('/fizzbuzz/<int:last_num>', methods=['Get'])
def fizzbuzz(last_num):
    for x in range(1, last_num):
        if x % 15 == 0:
            print("%s FizzBuzz" %x)
            continue
        elif x % 3 == 0:
            print("%sFizz" %x)
            continue
        elif x % 5 == 0:
            print("%s Buzz" %x)
            continue
        else:
            print(x)
            continue
    return jsonify({'message': "print in console"})

if __name__ == '__main__':
    app.run(debug = True, port = 4000)
