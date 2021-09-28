from blueprints import post, comment
from flasgger import Swagger
from flask import Flask, render_template


# Constants


app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "SviatAPI",
    "universion": 3
}
app.config["SWAGGER"]["openapi"] = "3.0.2"
app.config['SECRET_KEY'] = "SECRET"
swagger = Swagger(app, template_file='./swagger/config.yml')

app.register_blueprint(post, url_prefix='/posts')
app.register_blueprint(comment, url_prefix='/comment')


@app.route('/')
def index():
    return render_template('base.html', title='Custom Title', menu=['Posts'])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9003)
