#!/usr/bin/env python3
"""
Setting up a basic Flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders the homepage of the Flask application.

    This function handles the routing
    for the root URL ("/") of the application.
    It uses the Flask `render_template`
    function to render the '0-index.html' template.

    Returns:
        str: The rendered HTML content of the homepage.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port="5000", host="0.0.0.0", debug=True)
