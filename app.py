from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de Compra 1',
        'items': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.99
            }
        ]
    }

]

#GET purchase_orders
#GET purchase_orders
#POST purchase_orders
#GET purchase_orders_items
#POST purchase_orders_items

@app.route('/') #Decorator(Nenhum endpoint foi passado, então utilizaremos o localhost raiz)
def home():
    return "Hello World! Alterado"

@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id():
    for po in get_purchase_orders:
        if po ['id'] == id:
         return jsonify(po)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})    
app.run(port=5000)