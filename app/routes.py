from flask import Flask, jsonify, request

# Creating and instance of the flask class and assigning it to the variable app
# __name__ is a special Python variable that represents the name of the current module
app = Flask(__name__)

# Route to the home page where users can see all the articles listed down
@app.route('/', methods=['GET'])
def home_page():
    # Fetch all the articles and return the data to the frontend
    return

# Route to view a specific article
@app.route('/article/<slug>', methods=['GET'])
def fetch_article(slug):
    # Fetch the data related to the article and store in the template values
    return