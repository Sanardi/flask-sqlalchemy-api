# Flask Tech Test

## Getting Started

This project uses python3. A pip requirements.txt file is included to install the dependencies (SQLAlchemy, Dictalchemy, Flask)

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
