from flask import Flask, request, jsonify

from multiprocessing_array import data

app = Flask(__name__)

product_list = [
{
"id": 1,
"name": "TV",
"price": 20000,
"category": "Electronics"
},
{
"id": 2,
"name": "Mobile",
"price": 15000,
"category": "Electronics"
}
]


# 1. GET - Read all products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(product_list), 200


# 2. GET - Read one product
@app.route("/product/<int:id>", methods=["GET"])
def get_product(id):

    for product in product_list:
       if product["id"] == id:
          return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


# 3. POST - Create a product
@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()

    name = data["name"]
    price = data["price"]
    category = data["category"]

    if not name or not category or price <= 0:
        return jsonify({"error": "Invalid product data"}), 400

    new_id = len(product_list) + 1

    new_product = {
        "id": new_id,
        "name": name,
        "price": price,
        "category": category
    }

    product_list.append(new_product)

    return jsonify(new_product), 201


# 4. PUT - Update a product
@app.route("/product/<int:id>", methods=["PUT"])
def update_product(id):
    data = request.get_json()

    for product in product_list:
        if product["id"] == id:
            product["name"] = data["name"]
            product["price"] = data["price"]
            product["category"] = data["category"]

            return jsonify(product), 200

    return jsonify({"error": "Product not found"}), 404


# 5. DELETE - Delete a product
@app.route("/product/<int:id>", methods=["DELETE"])
def delete_product(id):
    for product in product_list:
        if product["id"] == id:
            product_list.remove(product)

            return jsonify({
                "message": "Product deleted successfully",
                "deleted_product": product
            }), 200

    return jsonify({"error": "Product not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)