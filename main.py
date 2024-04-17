from flask import Flask
from src.utils import generate_resume, get_resume

app = Flask(__name__, static_folder="public", static_url_path="")


@app.route("/")
def get_index():
    return get_resume()


@app.route("/generate_resume")
def post_generate_resume():
    generate_resume()
    return get_resume()


if __name__ == "__main__":
    generate_resume()
    app.run(host="0.0.0.0", port=80, debug=True)

