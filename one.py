from flask import Flask

app = Flask(__name__)

@app.route('/nama')
def nama():
    return "halaman nama"


if __name__ == '__main__':
    app.run(debug=True)