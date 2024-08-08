from flask import Flask, render_template, request
from functional_logic.api import most_stars_repos
from functional_logic.exceptions import GitHubApiException

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Typescript", "Go"]

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        selected_languages = available_languages
    elif request.method == 'POST':
        selected_languages = request.form.getlist("languages")

    results = most_stars_repos(selected_languages)

    return render_template(
        'index.html',
        results = results,
        available_languages = available_languages,
        selected_languages = selected_languages
    )

@app.errorhandler(GitHubApiException)
def handle_api_error(error):
    return render_template('error.html', message=error)