# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for, jsonify
from script import main

# Initialize the Flask app
app = Flask(__name__)

# Route for displaying all posts
@app.route('/')
def index():
    print("Index")
    return jsonify("Hello 11")

@app.route('/tweetsearch')
def intweetsearchdex():
    r = main()
    return jsonify(r)



# Run the app
if __name__ == '__main__':
    app.run(debug=True)
