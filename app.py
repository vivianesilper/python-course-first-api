from flask import Flask, jsonify, request

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

@app.route('/') #Decorator(Nenhum endpoint foi passado, então utilizaremos o localhost raiz)
def home():
    return "Hello World! Alterado"

@app.route('/purchase_orders', methods=['GET'])
def get_purchase_orders():
    return jsonify(purchase_orders)

@app.route('/purchase_orders/<int:id>')
def get_purchase_orders_by_id(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po)
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})


@app.route('/purchase_orders/<int:id>/items')
def get_purchase_orders_items(id):
    for po in purchase_orders:
        if po['id'] == id:
            return jsonify(po['items'])
        
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})

@app.route('/purchase_orders/<int:id>/items', methods=['POST'])
def create_purchase_orders_items(id):
    req_data = request.get_json()
    for po in purchase_orders:
        if po['id'] == id:
            po['items'].append({
                'id': req_data['id'],
                'description': req_data['description'],
                'price': req_data['price']
            })

            return jsonify(po['items'])
    return jsonify({'message': 'Pedido {} não encontrado'.format(id)})    

if __name__ == '__main__':
    app.run(port=5000)
