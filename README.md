# Youtube-API - A simple Youtube API web application to fetch youtube videos of a channel using youtube-api-v3 with Django Rest Framework, Javascript, HTML and CSS

## Requirements
- Python 3.10.4
- Django 4.0.6
- Django Rest Framework 3.13.1

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command
```
python3 -m venv venv

```
After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running
```
pip install -r requirements.txt

```
## Backend Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our 
application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized 
around collections and elements, both of which are resources.

All the endpoints start with `http://127.0.0.1:8000/`. The endpoints are given below-

| EndPoint  | HTTP Method | CRUD Method  | Result |
| ------------- | ------------- | ------------- | ------------- |
| api/v1/home/  | GET  | READ  | Get list of youtube videos  |
| api/v1/performance/  | GET  | READ  | Get list of filtered videos by performance  |
| api/v1/tag/  | GET  | READ  | Get list of filtered videos by tag  |

( Note - Filter by performance is done by sorting the videos based on their views as no metric was found to get the first hour views of a video from youtube-api-v3.) 

THe application uses a scheduler to update the youtube videos view count every minute so that filtering by performance is done on current view count of the videos.  

## Frontend Structure
The frontend of the web application is built on HTML, CSS and Javascript. The base index/homepage is rendered via django's template engine.
All data is being consumed by the rest API's using JavaScript.  


## Running the server
To run the server user the commands below -
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver --noreload 
```

## Testing
To test the endponts we can run the custom test cases by running the command below -
```
python manage.py test
```
