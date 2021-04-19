## Version

1.0.0

## How to run the application

### With Docker

To run the application, just run the docker-compose:

```bash
$ docker-compose up
```

or you can run 

```bash
$ ./scripts/start.sh
```

In the ``scripts`` folder, we also have a script to stop the server and to run the tests in the container.

We have two services:

    - nginx: we use nginx to server the application
    - server: the application

Then you can go to ```localhost``` or your ip address to start playing around.

### Without docker

#### Set-up virtualenv

**Note:** here we use python 3.8 as the python interpreter.

1. Create virtualenv:
```bash
$ virtualenv -p python3.8 venv
```

2. Activate virtualenv
```bash
$ source ./venv/bin/activate
```
**Note:** In order to exit from virtual environment use `deactivate`

3. Install all python core libraries
```bash
$ pip install -r requirements.txt
```

#### Execution

You can run the application by executing the module ``server/run.py``. This will run the application on localhost and the default port is 5000.

## Tests

We use pytest to execute the tests. Just run in the terminal

```bash
$ pytest --cov=server tests/
```

and (hopefully) all the tests should pass.
    