from flask import Flask, jsonify

app = Flask(__name__)

name = "نام"
family = "نام خانوادگی"

@app.route('/get_data', methods=['GET'])
def get_data():
    data = {
        'Name': name,
        'Family': family
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
