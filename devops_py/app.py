from flask import Flask, jsonify ,request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello From Python........."


@app.route('/health')
def health():
    return jsonify(status='ok',service='flask-app')

@app.route('/greet/<name>')
def greet(name):
    return jsonify(message=f'Hello,{name},Welcome to Flask..')

@app.route('/add',methods=['POST'])
def add_num():
    data=request.get_json()
    a=data.get('a')
    b=data.get('b')
    if a is None or b is None:
        return jsonify(error='Please Provide a and b '),400
    return jsonify(result=a+b)

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)