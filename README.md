# PawClubs
With Pawclubs, I try to build a community mainly around dogowners and dogsitters in co-working spaces and dog-friendly companies inorder to make the life easier for dogs who are brought to the working spaces and the owners to catch up with their daily activities. Besides dogsitting, other services such as dog events, dog training, etc. are offred to the community members.
# About the Web Application
 Aplication Architecture :
- Programming Language --> python3 / HTML-CSS
- Web Framework --> Flask
- Relational Database Management System --> SQLite
# Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

# Prerequisites and Installing
- You need to install python3, flask, pip & virtualenv.

To start, first create the virtual environment.
```
python3 -m venv venv
```
Activate the virtual environment.
```
source venv/bin/activate
```
Install Flask (Use pip).
```
pip install Flask
```
# Starting the Server
Clone my repository on github via this command:
```
git clone https://github.com/BehnazDer/foundation_project.git
cd my_project
```
If the virtual environment is not activated, first activate it :
```
source venv/bin/activate
```
Run Flask:
```
cd my_project
FLASK_APP=auth.py
flask run 
```
To run the server in the development mode add:
```
export FLASK_ENV= development
flask run
```
Serving on http://127.0.0.1:5000








