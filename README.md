# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```
### Trello Setup

---Setup a Trello Account
https://trello.com/signup

---Generae API Key and Token by following the link below
https://trello.com/app-key

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

Add API Key and API Server Token which you obtained from Trello to '.env' file. You can add Trello BoardId too to '.env'. Please note, never commit your secreat keys to Git 

Pytest Fixture has web browser defined and associated drivers are installed, should web browser updates, appropriate drivers will be required


## Running Tests

Two Test Folders have been added:
-C:\GitBash\DevOps-Course-Starter\test_ut\
-C:\GitBash\DevOps-Course-Starter\test_ete\

Three Test files are created
-C:\GitBash\DevOps-Course-Starter\test_ut\test_view_model.py
-C:\GitBash\DevOps-Course-Starter\test_ete\test_app.py
-C:\GitBash\DevOps-Course-Starter\test_ete\test_trello_calls.py

To run all tests, please run following command

```bash
$ poetry run pytest
```

To run individual test files, please navigate to the file and run the command as below
below command run tests in test_trello_calls.py file

```bash
$ poetry run pytest test_ete\test_trello_calls.py 
```

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running the App on Managed Node by providing commands via Ansible Playbook from Control Node

### Provision VM through ansible control node
* set up an SSH key pair
* Run ssh-keygen to generate an SSH key pair. This will generate it in the ec2-user's `.ssh`
 directory
* Use the ssh-copy-id tool, specify the host VM's address. In our case its 35.178.233.144
* For ease, install Remote -SSH extension on VS Code, this will allow you to connect to VMS
ssh command you will need is : ssh ec2-user@ipaddress | in our case its ssh ec2-user@35.178.233.144
* to run ansible playbook, please use the command below
`ansible-playbook ansible_playbook.yml -i ansible_inventory_file`


### api server token
* when ansible playbook is run, it will prompt 'what is your api server token'
 please insert api server token, this is not purposefully migrated to host node for security 

## How to build and run development and production containers

* to build production container from a multi-stage Dockerfile
`docker build -t production --target production .`
* to run the docker container for production
` docker run --env-file .env -p 8000:8000 -it production `
` (-it runs docker interactively) `

* to build development container from a multi-stage Dockerfile
`docker build -t development --target development .`
* to run the docker container for development (without mount)
`docker run --env-file .env -p 8000:5000 -it development`
* to run the docker container for development using mount, so Flask automaticlaly reloads when we edit Python files
`docker run --env-file ./.env -p 5100:5000 --mount type=bind,source="$(pwd)"/todo_app,target=/opt/todo_app development`

