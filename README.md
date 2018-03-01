# Anchor-Capstone

## GitHub

[Project Repo](http://github.com/westinrc/Anchor-Capstone)

## Table of Contents

* [Getting Started](#getting-started)
    1. [Installing pip](#installing-pip)
    1. [Installing Virtual Environment](#installing-a-virtual-environment)
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)

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

Loading the pitt data
http://0.0.0.0:[localhost]/upload-pitt-delimited
body must have form data of file pitt-delimeted (with that name!)

Hit the load-icd9-structure
http://0.0.0.0:[localhost]/load-icd9-structure

Build the representation (roughly 5min)
http://0.0.0.0:[localhost]/build-structured-rep

Pre Process Patients
http://0.0.0.0:[localhost]/preprocess-patients
pass the max_patients in via a json object i.e.:
{
    "max_patients": 93422
}