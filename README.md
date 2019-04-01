# Flask Tech Test

## Getting Started

This project uses python3. A pip requirements.txt file is included to install the dependencies (SQLAlchemy, Dictalchemy, Flask)

### Creating a Python 3 virtual environment
- To run the application in a virtual Python environment, follow these instructions. This example will create a virtual Python environment for 3.4.8

- Check you have the pynv version you need:
pyenv versions

- You should see 3.4.8

- If you do not have the correct version of Python, install it like this:
pyenv install 3.4.8

- On command line do this:
~/.pyenv/versions/3.4.8/bin/python -m venv env


- This creates a folder called env. Then do this to activate the virtual environment:
source env/bin/activate

- Lastly do this to check that you are now on the correct Python version:
python --version

To check we are on the right Python version

- You can install the dependencies with `pip install -r requirements.txt`

- You can then run the app with `flask run` or `python app.py` in the root directory

## Provided Extras
- A sample Dockerfile is provided that will run the application in an isolated environment
- A postman collection is provided in `flask-tech-test.postman_collection.json` that contains List/Create/Read/Update/Delete samples.

## Tasks

- Add an new entity called `Author` with a `firstName` and a `lastName`. An API user should be able to create a new `Author`, edit an existing one and list all existing ones.
- Update the `Article` entity so that it relates to an `Author`. An API user should now be able to select an `Author` when creating or editing an `Article`.

## Project Structure Notes

- The database models are stored in the `techtest/models` folder
- The routes of the Flask app are in `techtest/routes` folder

In both cases, the modules are loaded by using the `__all__` variable in `__init__.py`, so be sure to update this if you add new files.
