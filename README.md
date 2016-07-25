Face-Off ![Build Status](https://travis-ci.org/excellalabs/face-off.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/excellaco/face_it/badge.svg)](https://coveralls.io/r/excellaco/face_it)

=======================

A Yammer/Django Application application built for the gamification of learning the names of your fellow colleagues.
One difficult part of joining a new company is putting names to faces. Utilizing Yammer OAuth, this webapp can make the learning process more fun.

# Quick-Start Guide
-----
### 1. Yammer Client Application
* [Register An App With Yammer](https://developer.yammer.com/v1.0/docs/app-registration)
* **Note** the Redirect URI & Javascript Origins field
    * Dev:
        * Redirect URI - `http://localhost:8111/complete/yammer/`
        * Javascript Origins - `http://localhost:8111`
    * Production:
        * replace dev fields with respective hostname 
    * Once you register, you'll receive a `Client ID` and `Client Secret`. Copy these keys, as you'll need to plug them into your application settings.


### 2. Development Environment Setup
* Clone this repo
* Copy `face_it/settings/local.py.example` to `face_it/settings/local.py`
* Add your keys (created in step 1) to `face_it/settings/local.py`
* Install [Vagrant](https://www.vagrantup.com/) and [Virtualbox](https://www.virtualbox.org/)
* Initialize the vagrant box - `vagrant up`
* Log into the server - `vagrant ssh`
* Create a super user using the command `python manage.py createsuperuser`
* Install & Start [Redis Cache server](http://redis.io/) prior in a separate shell - `redis-server` 
* Launch the app - `python manage.py runserver 0.0.0.0:8000`
* Access the app in your browser - `http://localhost:8111`

### 3. Heroku Deployment (Optional)
---
**Required Items**
* Redis Server
* AWS Bucket
* Postgres Server

--------------
####Steps
* `heroku create {appName}`
* `heroku config:add BUILDPACK_URL=https://github.com/ddollar/heroku-buildpack-multi.git`
* `git push heroku master`
* `heroku addons:add heroku-postgresql`
* Create a [RedisToGo](https://redistogo.com) account
    * `heroku addons:add redistogo`
    * `heroku config:add REDISTOGO_URL={instanceName}` 
        *  i.e instanceName = redis://redistogo:xxxx@test.redistogo.com:10355/
* Create an [AWS account](http://aws.amazon.com/s3/) to have access to an [AWS Bucket](http://docs.aws.amazon.com/AmazonS3/latest/gsg/CreatingABucket.html)
    * Create environment variables specific for the created aws bucket:
        *  AWS_ACCESS_KEY_ID
        *  AWS_SECRET_ACCESS_KEY
        *  AWS_STORAGE_BUCKET_NAME
* `heroku ps:scale web=1`
* `heroku run python manage.py syncdb`

####**Required Environment Variables Checklist**

|Environmental Variable Name|Value (example)|
|---------------------------|:-------------:|
|SOCIAL_AUTH_YAMMER_KEY|xxxxxxx|
|SOCIAL_AUTH_YAMMER_SECRET|xxxxxxx|
|NPM_CONFIG_PRODUCTION|true|
|DJANGO_SETTINGS_MODULE|face-off.settings.production|
|REDISTOGO_URL|redis://redistogo:xxxx@test.redistogo.com:10355/|
|AWS_ACCESS_KEY_ID|xxxx|
|AWS_SECRET_ACCESS_KEY|xxxx|
|AWS_STORAGE_BUCKET_NAME|xxx-bucket|

## Tests
---
### Unit Tests
* Load test fixture data `./manage.py loaddata "core/fixtures/core-test.json"`
    * Applying fixtures pushes pre-populated data into your application.
* Run unit-tests - `python manage.py test`
 
#### Selenium Tests w/ Behave
* start behave instance - `behave core/features`


## Data Stored
* Yammer related Data
    * First Name
    * Last Name
    * Email
    * Yammer profile page link
    * Network Name
