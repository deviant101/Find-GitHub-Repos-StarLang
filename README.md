# GitHub Repository Search Flask App

This Flask application uses the GitHub Search API to find repositories with the most stars based on selected programming languages.

## Features

- Search for GitHub repositories by programming languages.
- Display repositories with the most stars.
- Handle errors gracefully with user-friendly messages.

## Prerequisites

- Python 3.6+

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/deviant101/Find-GitHub-Repos-StarLang.git
    cd Find-GitHub-Repos-StarLang
    ```

2. Create a virtual environment:

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install the required packages:

    ```sh
    python -m pip install -r requirements.txt
    ```

## Running the App

1. Start the Flask app:

    ```sh
    FLASK_APP=app.py flask run
    ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

## Usage

- Select the programming languages you want to search for.
- Click the "Search" button to fetch repositories with the most stars.
- The results will be displayed on the same page.

## Project Structure

- `app.py`: Main application file containing routes and views.
- `functional_logic/api.py`: Contains functions to interact with the GitHub API.
- `functional_logic/models.py`: Defines the data models.
- `templates/`: Contains HTML templates for rendering views.
- `static/`: Contains static files like CSS.

## Error Handling

- Errors related to the GitHub API are handled gracefully and displayed using the `error.html` template.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.