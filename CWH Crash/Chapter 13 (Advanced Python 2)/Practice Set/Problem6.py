# Run pip freeze for the system interpreter. Take the contents and create a similar virtualenv

#* Follow these steps:
'''
Open the code folder in terminal

pip freeze > requirements.txt

virtualenv env    --> Creates a new virtual environment

.\env\Scripts\activate.ps1

pip install -r requirements.txt

'''