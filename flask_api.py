from flask import Flask

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello Firestarter!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)

#curl -v -G http://localhost:105/hello/

