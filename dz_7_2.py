import os


def main():
    os.system('touch my_project/settings/__init__.py')
    os.system('touch my_project/settings/dev.py')
    os.system('touch my_project/settings/prod.py')
    os.system('touch my_project/mainapp/__init__.py')
    os.system('touch my_project/mainapp/models.py')
    os.system('touch my_project/mainapp/views.py')
    os.system('mkdir my_project/mainapp/templates')
    os.system('mkdir my_project/mainapp/templates/mainapp')
    os.system('touch my_project/mainapp/templates/mainapp/base.html')
    os.system('touch my_project/mainapp/templates/mainapp/index.html')
    os.system('touch my_project/authapp/__init__.py')
    os.system('touch my_project/authapp/models.py')
    os.system('touch my_project/authapp/views.py')
    os.system('mkdir my_project/authapp/templates')
    os.system('mkdir my_project/authapp/templates/authapp')
    os.system('touch my_project/authapp/templates/authapp/base.html')
    os.system('touch my_project/authapp/templates/authapp/index.html')