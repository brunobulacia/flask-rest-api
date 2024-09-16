from flask import Flask
from flask_cors import CORS
from binary_search_tree import BinarySearchTree as BST

app = Flask(__name__)
CORS(app)  # Esto permite CORS para todas las rutas y orígenes
tree = BST()

@app.route('/api', methods=['GET'])
def get_tree_nodes():
    return tree.level_order_traversal()

@app.route('/api/insert/<int:data>', methods=['POST'])
def insert_node(data):
    tree.insert(data)
    return {'message': f'Nodo {data} insertado con éxito'}, 200

@app.route('/api/delete/<int:data>', methods=['DELETE'])
def delete_node(data):
    tree.delete(data)
    return {'message': f'Nodo {data} eliminado con éxito'}, 200

@app.route("/api/clear", methods=['DELETE'])
def clear_tree():
    tree.clear()
    return {"message": "Arbol limpio"}, 200

if __name__ == '__main__':
    app.run(debug=False)
