# try-redis

Try redis is a Django application that is made to demonstrate my ability in:

 - Using Redis as a:
	 - Cache
	 - Message Queue

This application also uses Firebase Cloud Messaging to deliver push notifications, though it is only able to do that to the device where the server is deployed.

# How to Setup

## Install PyEnv
I developed this application using [PyEnv,](https://github.com/pyenv/pyenv) which is used as an easy way to manage the Python Versions that are used to develop the application. Through PyEnv, I used Python version 3.9.7. Therefore, please [install PyEnv first](https://github.com/pyenv/pyenv) (the link will take you to PyEnv's github page, where you can see the instructions for installing PyEnv in various OSes, and use the command to install Python version 3.9.7 through PyEnv:

`pyenv install 3.9.7`

## Install Redis

After that, you can install Redis. In the case of this app, I assume that Redis will be installed using the default settings on your devices.

## Install Dependencies

After you've installed both PyEnv and Redis, you will need to install the dependencies through PyEnv so that the installation of the dependencies will be local. To do that, you can use this command:

`pipenv install --dev`

## Do some Django Housekeeping

There are some things that you should do before running a Django App, namely:

 1. Migration
 2. Collection of Static Files
 3. Creation of a Super User Account

### Migration
To make sure that the database has the needed fixtures, you will need to migrate them.

`pipenv run python manage.py migrate`

### Collection of Static Files
There are some static files that this app serves. To make sure that the static files have been collected and ready to be served, use this command:

`pipenv run python manage.py collectstatic`

### Creation of a Super User Account
To be able to access the admin site, you will need to create a super user. To do that, you can use this command:
`pipenv run python manage.py createsuperuser`

# Setting up Firebase Keys

Before doing this step, please refer to the "How to Setup" section to properly setup the app.

Go to the Firebase Console, create a new project, then create a new app. Paste the `const firebaseConfig` dictionary on the file, replacing the currently available but blank firebaseConfig.

Then, replace the empty vapidkey value by generating one at the Web Push certificates section of the web configuration of the Cloud Messaging settings on Firebase.

Also in the Cloud Messaging settings is the server key. Copy the server key, and paste it into the .env file as follows:

    ...
    FCM_API=<insert server key here>
    ...

Start the app using

`pipenv run python manage.py runserver`

Then, obtain the Firebase Registration ID by going to this endpoint assuming that you are using the default ip and ports for Django:

`localhost:8000/redis_as_cache/fetchtoken/`

Then, look into the console and copy the ID there and paste it to the .env file as follows:

    ...
    FIREBASE_REGISTRATION_ID=<insert id here>
    ...
Also, paste the firebase url to the .env file as follows:
   
    ...
    FIREBASE_URL='https://fcm.googleapis.com/fcm/send'
    ...

# Starting up the App 

After setting up the app and the firebase keys, open a terminal window and run Redis by using (in Ubuntu):

`redis-server`

Then open another terminal window and run the default worker for [django-rq](https://github.com/rq/django-rq) by using this command:

`pipenv run python manage.py rqworker default`

Please do keep in mind that rqworker does not support hot reload. Therefore, if the app reloads for any reason (usually when modifying files), please stop the app by using `CTRL + C` and run the default worker again.

Finally, start the app using 

`pipenv run python manage.py runserver`

