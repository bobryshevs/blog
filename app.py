from flask import Flask, render_template
from flasgger import Swagger
from blueprints import post, comment


# Constants


app = Flask(__name__)
swagger = Swagger(app)
app.config['SECRET_KEY'] = "SECRET"

app.register_blueprint(post, url_prefix='/posts')
app.register_blueprint(comment, url_prefix='/comment')


@app.route('/')
def index():
    return render_template('base.html', title='Custom Title', menu=['Posts'])


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9003)
