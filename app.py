from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/http_trigger', methods=['GET', 'POST'])
def http_trigger():
    # GET パラメータの取得
    name = request.args.get('name')

    # POST の JSON ボディから取得
    if not name and request.is_json:
        name = request.json.get('name')

    # レスポンスの生成
    if name:
        return jsonify({"message": f"Hello, {name}. This Flask app executed successfully."})
    else:
        return jsonify({"message": "This Flask app executed successfully. Pass a name in the query string or in the request body for a personalized response."})

if __name__ == '__main__':
    app.run(debug=True)
