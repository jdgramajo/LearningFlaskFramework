from flask import Flask, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name is None:
        name = request.args.get('name')
    if name:
        return 'Hello %s' % name
    else:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)
