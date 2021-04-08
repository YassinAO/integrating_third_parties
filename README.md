# Integrating third parties

## About
For this case we’ll make use of a common situation at Maykin Media: integrating third parties in a 
piece of software. These third parties expose data or API’s which are used in the services that we 
offer our clients.

In this case, to keep the exercise small, an application has to be built that imports CSV hotel data. Of 
course CSV data is flat, while in the case of data models in Django one wants to make use of relations.
So during the import of the data those relations have to be restored. Then in the end a small frontend application has to be built that allows users to lookup hotel data.


## Requirements
* Python V3.+
* Latest Django version


## Installation

```
git clone https://github.com/YassinAO/integrating_third_parties
cd integrating_third_parties
pip install pipenv 
pipenv shell
pip install -r requirements.txt
copy .env-boilerplate .env
```
#### **Make sure to change the credentials in the .env file to fit your needs.**

Once you have the database up and running, use the following commands:
```
python manage.py makemigrations
python manage.py migrate
```
To run the server use the command:
```
python manage.py runserver
```