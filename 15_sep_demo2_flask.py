# flask get post

from flask import Flask, jsonify, request, make_response

app=Flask(__name__)

income = [
    {"description":"salary", "amount":5000}
]

@app.route("/incomes")
def get_incomes():
    return jsonify(income)

@app.route("/incomes", methods=["POST"])
def add_income():
    income.append(request.get_json())
    return 'Created', 201

stock={
    "fruit":{
        "apple":100,
        "banana":45,
        "cherry":1000
    },
    "vegetable":{

    }
}

@app.route("/stock")
def get_stock():
    res = make_response(jsonify(stock),200)
    return res

@app.route("/stock/<collection>")
def get_collection(collection):
    if collection in stock:
        res = make_response(jsonify(stock[collection]), 200)
        return res
    res = make_response(jsonify({"error": "Not found"}), 400)
    return res

@app.route("/stock/<collection>/<member>")
def get_member(collection, member):
    if collection in stock:
        member = stock[collection].get(member)
        if member:
            res = make_response(jsonify(member), 200)
            return res
        res = make_response(jsonify({"error":"Not found"}), 404)
        return res

# 1 update based on the key or member
# 2 instead create return the error code
@app.route("/stock/<collection>", methods=["PUT"])
def put_collection(collection):
    req = request.get_json()
    if collection in stock:
        stock[collection] = req
        res = make_response(jsonify({"msg":"collection updated.."}), 200)
        return res
    # either create or we need send error saying record not found for updation
    else:
        res = make_response(jsonify({"error": "Not found"}), 400)
        return res
    # stock[collection] = req
    # res = make_response(jsonify({"msg":"collection created..."}), 201)
    # return res
@app.route("/stock/<collection>", methods=["DELETE"])
def delete_collection(collection):
    if collection in stock:
        del stock[collection]
        res = make_response(jsonify({"msg": "Deleted.."}), 204)
        return res
    else:
        res = make_response(jsonify({"msg": "Collection not found.."}), 404)
        return res

# deleting member
@app.route("/stock/<collection>/<member>", methods=["DELETE"])
def delete_member(member,collection):
    if collection in stock:
        if member in stock[collection]:
            del stock[collection][member]
            res = make_response(jsonify({"msg": "Deleted.."}), 204)
            return res
        else:
            res = make_response(jsonify({"msg": "Member not found.."}), 404)
            return res
    res = make_response(jsonify({"msg": "Collection not found.."}), 404)
    return res

if __name__=='__main__':
    app.run(debug=True, port=5001)