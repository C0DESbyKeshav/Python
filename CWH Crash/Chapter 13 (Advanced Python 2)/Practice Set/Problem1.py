# Create two virtual environments, install few packages in the first one. How do you create the similar environment in the second one ?

# * FOLLOW THE FOLLOWING STEPS:
# * INSTALLATION
''' To use virtual environments, we write
pip install virtualenv  --> Install the package

We create a new environment using:
virtualenv env    --> Creates a new virtual environment

The next step after creating the virtual environment is to activate it.
- Open the code folder in terminal
- pip install pandas
- .\env\Scripts\activate.ps1

We can now use this virtual environment as a separate python installation.'''

# * pip freeze command
'''pip freeze returns all the packages installed in a given python environment along with the versions.

pip freeze > requirements.txt
The above command line creates a file named requirements.txt in the same directory containing the output of pip freeze.

We can distribute this file to other users and they can recreate the same environment using:
pip install -r requirements.txt
'''
