# flask-template-2023

A web application starter template written in Python with the Flask framework.


## Repo Setup

Make a copy of this template repo (as necessary). Clone your copy of the repo onto your local machine. Navigate there from the command-line.

Setup and activate a new Anaconda virtual environment:

```sh
conda create -n flask-template-2023 python=3.10
conda activate flask-template-2023
```

Install package dependencies:

```sh
pip install -r requirements.txt
```

## Services Setup

  + [Google Cloud](/setup/GOOGLE_CLOUD.md)
  + [Google Login](/setup/GOOGLE_LOGIN.md)


## Configuration

Create a new file called ".env" in the root directory of this repo, and paste inside the following contents:

```sh
# this is the ".env" file...

# for flask:
FLASK_APP="web_app"

# for google login:
GOOGLE_CLIENT_ID="___________"
GOOGLE_CLIENT_SECRET="___________"
```

## Usage

Run the web application, then view in the browser at http://localhost:5000/:


```sh
# if you have configured the FLASK_APP environment variable already:
flask run
```

Alternatives:

```sh
# Mac OS:
FLASK_APP=web_app flask run
```

```sh
# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP="web_app" variable via ".env" file
export FLASK_APP=web_app
flask run
```

Press "control+c" or "ctrl+c" to stop the web server when done.
