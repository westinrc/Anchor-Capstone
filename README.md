# Anchor-Capstone

# Table of Contents
* [Getting Started](#getting-started)  
    1. [Installing pip](#installing-pip)
    2. [Installing Virtual Machine](#installing-a-virtual-machine)  
* [Versioning](#versioning)
* [Authors](#authors)
* [License](#license)

# Getting Started
The following instructions will get the project up and running locally for development and testing purposes.

## Installing pip
This project uses Python-Flask, one of the tools that will be needed is to have pip installed on your machine. If you do not currently have this setup you can find many how-to resources online, however we will give a brief overview of the process.

The easiest way to install pip is using the easy_install option. If this does not work I would recommend viewing online resources as mentioned above.
```
$ sudo easy_install pip
```

If you need to simply check your current version or find out if python is installed, you can do so by running the following.
```
$ python --version
```
If no version is returned then use online resources to install python onto your machine.

## Installing a virtual machine
When running projects locally you will need to ensure that your machine version of python is not being changed, MacOS 10.11 will give errors indicating that you are not able to change the version on your machine. Thus we can get around this issue by installing a "Virtual Environment" (virtualenv) that your machine can use for a specified directory. The folowing will walk you through the install and setup process.

If you are using MacOS X or Linux the below should install the virtualenv
```
$ sudo pip install virualenv
```

If you are running Ubuntu you can try
```
$ sudo apt-get install python-virtualenv
```

Once virtualenv has been installed you can create a project directory (where you will store the project). i.e.
```
$ mkdir anchorProject
$ cd anchorProject
$ virtualenv venv
```
Now the virtualenv has been created in that directory and you need to simply activate and deactivate as needed when running the project.
To activate on MacOS X or Linux do the following:
```
$ source venv/bin/activate
```
To activate on Windows:
```
$ venv\Scripts\activate
```
To deactvate on any of the aforementioned operatings systems:
```
$ deactivate
```

# Versioning
We use [SemVer](http://semver.org/) for versioning. 

# Authors
* [Westin Christensen](https://github.com/westinrc) </br>
* [Dhalton Huber](https://github.com/Dhalton95) </br>
* [Karl Noss](https://github.com/n055) </br>
* [Tori Ottenheimer](https://github.com/vottenhe) </br>
* [Andreas Regus](https://github.com/aregus) </br>

# License
