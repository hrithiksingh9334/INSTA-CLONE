# Django and React integration #

This web application consists on a basic personal blog to make posts, to create categories, this also includes featured posts shown on slider, comments on each post and uploading content of categories and posts (text and images) using Django admin and the data is shown on a react frontend application.

## Example ##
![Example](https://user-images.githubusercontent.com/59356298/102147219-66e05280-3e38-11eb-8f5f-f6e9d18795a1.png)

## Programming languages (frameworks, libraries) ##
*   Django (Django rest framework, Django models, Django admin, JSON, serialization)
*   Reactjs (HTML, CSS, reactstrap, react redux, react route, JSON)

## Database ##
*   MySQL

## Installation ##
*   First create a MySQL database named "posts" 
*   Create a virtual enviroment for the django dependencies [Link official documentation](https://docs.djangoproject.com/en/3.1/intro/contributing/#getting-a-copy-of-django-s-development-version "djangoenviroment")
*   Activate the enviroment and go to the backend_django folder and install the Django dependencies with the following command using the requirements.txt file which has the dependencies
	* ### `pip install -r requirements.txt`
*   To create the tables on the database, on the backend_django folder run the following commands (python or python3 depends on your configuration when the enviroment variable on the system was set up)
	* ### `python manage.py makemigrations`
	* ### `python manage.py migrate`
*   To upload the content using Django admin, a super user has to be created, see official documentation [Link official documentation Django admin](https://docs.djangoproject.com/en/3.1/intro/tutorial02/#introducing-the-django-admin "djangoenviroment")
*   To install the react application, go to the frontend_reactjs folder and run
	* ### `yarn install`

## How to run it ##
*   Go to the backend_django folder and run
	* ### `python manage.py runserver`
*   Also go to the frontend_reactjs folder and run
	* ### `yarn start`

## Notes ##
*   If different ports are being used, go to the settings.py file and change the port in the whitelist, or change the port in the baseUrl.js file, it depends on the configuration.
*   This application is not using https yet, it uses http, when deploying the application, I suggest using https, a private key and a public key (SSL) for exchanging data between client and server for security.

## Credits ##
*   [Tutorial django rest framework](https://bezkoder.com/django-crud-mysql-rest-framework/ "djangorestframeworktutorial")