Face It ![Build Status](https://travis-ci.org/excellaco/face_it.svg?branch=master)
<a href='https://coveralls.io/r/excellaco/face_it'><img src='https://coveralls.io/repos/excellaco/face_it/badge.svg' alt='Coverage Status' /></a> 
=======================

A Django app for testing your ability to match coworker names with faces, utilizing the Yammer API.

Setup
-----

* Clone this repo
* Follow the instructions for setting up your Yammer App Keys [here](https://github.com/excellaco/yammer-hackathon/wiki/Yammer-OAuth-Setup)
* Copy `face_it/settings/local.py.example` to `face_it/settings/local.py`
* Add your keys to `face_it/settings/local.py`
* Install Vagrant and Virtualbox
* Initialize the vagrant box - `vagrant up`
* Log into the server - `vagrant ssh`
* Create a super user using the command `python manage.py createsuperuser`
* Start Redis Cache server prior in a separate tab - `redis-server` 
* Launch the app - `./manage.py runserver 0.0.0.0:8000`
* Access the app in your browser - `http://localhost:8111`
