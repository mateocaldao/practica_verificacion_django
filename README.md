#Practica_Verificacion_Django
##Synopsis
A simple poll app
##Isntallation
1. Clone the repo and install and create a new environment using [virtualenv](https://github.com/pypa/virtualenv):
`
source venv/bin/activate
`

2. Once you have created and activated the environment you have to install the dependencies:
`pip install -r requirements.txt`

##Tests
All TDD tests are into `tests`directory. You can run then using:
`coverage run manage.py test -v 2`

All BDD tests are into `features` directory. You can run then using:
`lettuce --verbosity=3`

Run the tests means: lint the code using PEP8 and pass all the tests

##Contributors
- Mateo Cerviño Aldao

##License
All the rights reserved (C) 2016
