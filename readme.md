# CS-235 Flix ASSIGNMENT 3

## Description

A web application that instances webpages for movies and implements Databases
## Installation

**Installation via requirements.txt**

A3

```shell
$ cd COMPSCI-235
$ py -3 -m venv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

When using PyCharm, set the virtual environment using 'File'->'Settings' and select 'Project:COMPSCI-235' from the left menu. Select 'Project Interpreter', click on the gearwheel button and select 'Add'. Click the 'Existing environment' radio button to select the virtual environment. 

## Execution

**Running the application**

From the *COMPSCI-235* directory, and within the activated virtual environment (see *venv\Scripts\activate* above):

````shell
$ flask run
```` 


## Configuration

The *COMPSCI-235/.env* file contains variable settings. They are set with appropriate values.

* `FLASK_APP`: Entry point of the application (should always be `wsgi.py`).
* `FLASK_ENV`: The environment in which to run the application (either `development` or `production`).
* `SECRET_KEY`: Secret key used to encrypt session data.
* `TESTING`: Set to False for running the application. Overridden and set to True automatically when testing the application.
* `WTF_CSRF_SECRET_KEY`: Secret key used by the WTForm library.


## Testing
From the COMPSCI-235 directory, and within the activated virtual environment (see venv\Scripts\activate above):

```
$ python -m pytest
```

**Important**
 
 in `A3\adapters\memomory_repository.py` the `load_movies_and_tags` method has a loop:
 
```def load_movies_and_tags(data_path: str, repo: MemoryRepository):
for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
```
and in `A3\adapters\database_repository.py` the `populate` function executes:
 
```
cursor.executemany(insert_movies, movie_record_generator(os.path.join(data_path, 'Data1000Movies.csv')))
```
to enable testing, the both paths must be changed to `test_movies.csv`

Testing requires that file *COMPSCI-235/tests/conftest.py* be edited to set the value of `TEST_DATA_PATH`. You should set this to the absolute path of the *COMPSCI-235/tests/data* directory. 

E.g. 

`TEST_DATA_PATH = os.path.join('C:', os.sep, 'Users', 'idenf', 'OneDrive', 'Documents', 'GitHub', 'COMPSCI-235', 'tests', 'data')`

assigns TEST_DATA_PATH with the following value (the use of os.path.join and os.sep ensures use of the correct platform path separator):

`C:\Users\idenf\Ondrive\Documents\GitHub\Compsci-235\tests\data`

You can then run tests from within PyCharm.

 
