import json
import logging
import os

from flask import Flask, flash, redirect, request, send_from_directory, session, url_for
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("recipy")

app = Flask(__name__)
CORS(app, expose_headers="Authorization")

def scrape(data):
    print(data)
    return data

def merge(ingredients):
    return ingredients

@app.route("/", methods=["POST", "GET"])
def generate_list():
    logger.info("Generating list.")

    list_of_recipes = json.loads(request.data)

    # scrapping
    ingredients = scrape(list_of_recipes)

    # merge ingredients
    merged_ingredients = merge(ingredients)

    print(merged_ingredients)

    return json.dumps(merged_ingredients)

if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run(debug=True, host="0.0.0.0", use_reloader=False)