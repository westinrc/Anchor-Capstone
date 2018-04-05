<<<<<<< HEAD
# Anchor-Capstone

## GitHub

[Project Repo](http://github.com/westinrc/Anchor-Capstone)

## Table of Contents

* [Getting Started](#getting-started)
    1. [Installing pip](#installing-pip)
    1. [Installing Virtual Environment](#installing-a-virtual-environment)
    1. [Installing Requirements](#installing-requirements-in-virtual-environment)
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)
* [Development Steps](#development-steps)

## Getting Started

The following instructions will get the project up and running locally for development and testing purposes.

### Installing pip

This project uses Python-Flask, one of the tools that will be needed is to have pip installed on your machine. If you do not currently have this setup you can find many how-to resources online, however we will give a brief overview of the process.

The easiest way to install pip is using the easy_install option. If this does not work I would recommend viewing online resources as mentioned above.

```bash
sudo easy_install pip
```

If you need to simply check your current version or find out if python is installed, you can do so by running the following.

```bash
python --version
```

If no version is returned then use online resources to install python onto your machine.

### Installing a virtual environment

When running projects locally you will need to ensure that your machine version of python is not being changed, MacOS 10.11 will give errors indicating that you are not able to change the version on your machine. Thus we can get around this issue by installing a "Virtual Environment" (virtualenv) that your machine can use for a specified directory. The folowing will walk you through the install and setup process.

If you are using MacOS X or Linux the below should install the virtualenv

```bash
sudo pip install virualenv
```

If you are running Ubuntu you can try

```bash
sudo apt-get install python-virtualenv
```

Once virtualenv has been installed you can create a project directory (where you will store the project). i.e.

```bash
mkdir anchorProject
cd anchorProject
virtualenv venv
```

Now the virtualenv has been created in that directory and you need to simply activate and deactivate as needed when running the project.
To activate on MacOS X or Linux do the following:

```bash
source venv/bin/activate
```

To activate on Windows:

```bash
venv\Scripts\activate
```

To deactvate on any of the aforementioned operatings systems:

```bash
deactivate
```

### Installing requirements in virtual environment

These steps only need to be performed the first time that you use a new virtual environment

To install the requirements activate your virtual environment as shown [above](#installing-a-virtual-environment).

navigate to folder api

```bash
Anchor-Capstone/api
```

in the terminal run

```bash
pip intstall -r requirements.txt
```

At this point you can now continue with the [development steps](#development-steps).

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* [Westin Christensen](https://github.com/westinrc) </br>
* [Dhalton Huber](https://github.com/Dhalton95) </br>
* [Karl Noss](https://github.com/n055) </br>
* [Tori Ottenheimer](https://github.com/vottenhe) </br>
* [Andreas Regus](https://github.com/aregus) </br>

## License

## Development Steps

Start The Development Server

```python
cd api/anchor_explorer

python anchor_explorer.py
```

In order to hit the endpoints you will need to use a program like [Postman](https://www.getpostman.com/)

`5000 is the typical port, but could differ`

Loading the pitt data (approx. 5 minutes) [Method : POST] </br>
http://0.0.0.0:5000/upload-pitt-delimited </br>
body must have form datsa of file pitt-delimeted (with that name!)

Hit the load-icd9-structure [Method : POST] </br>
http://0.0.0.0:5000/load-icd9-structure

Build the representation (approx. 5 minutes) [Method : POST] </br>
http://0.0.0.0:5000/build-structured-rep </br>
body must have a json object to be passed i.e.:
{
    "datatype": "code"
}

Pre Process Patients </br>
http://0.0.0.0:5000/preprocess-patients </br>
pass the max_patients in via a json object i.e.:
{
    "max_patients": 93422
}

### DO NOT PUSH THESE FILES

* anchor_explorer > utils > Structures Folder
* anchor_explorer > ICD9
* wordshelf.db
* visitshelf.db
* visitid

### Starting and stopping mysql server locally with brew

```bash
brew services start mysql

brew servies stop mysql
```

[Resource for more details on brew services](https://robots.thoughtbot.com/starting-and-stopping-background-services-with-homebrew)

[Resource for more details on writing markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

### Connecting to mysql

```bash
mysql -u capstone -p[password]
```

note that there is no space between the `-p` and password, do not use any brackets when writing the password.
||||||| merged common ancestors
# Anchor-Capstone
=======
# Anchor-Capstone


# Authors
Westin Christensen </br>
Dhalton Huber </br>
Karl Noss </br>
Tori Ottenheimer </br>
Andreas Regus </br>
>>>>>>> 110a03bbde1297d7af7643ce4873b0d4162096ba
