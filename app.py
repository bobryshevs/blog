import json
from blueprints import post, users
from flasgger import Swagger
from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException
from loggers_factory import loggers_factory
# Constants

logger = loggers_factory.get()
app = Flask(__name__)
app.config["SWAGGER"] = {
    "title": "SviatAPI",
    "universion": 3
}
app.config["SWAGGER"]["openapi"] = "3.0.2"
app.config["SECRET_KEY"] = "SECRET"
swagger = Swagger(app, template_file="./swagger/config.yml")

app.register_blueprint(post, url_prefix="/posts")
app.register_blueprint(users, url_prefix="/users")


@app.route("/")
def index():
    return render_template("base.html", title="Custom Title", menu=["Posts"])


# @app.errorhandler(Exception)
# @app.errorhandler(HTTPException)
# def handle_exception(e):
#     logger.warning("Inside_handle_exception")
#     logger.warning(str(e))
#     return jsonify({"error": str(e)}), 500


# app.register_error_handler(500, handle_exception)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=9003)
