[![CI](https://github.com/urbeingwatched8/devops/actions/workflows/github-actions-demo.yml/badge.svg?branch=master)](https://github.com/urbeingwatched8/devops/actions/workflows/github-actions-demo.yml)
## devops
#Lab1-2 
Created the simplest Python web app using Django and Sqlite3. Put it in the Docker container.
How to install Python:
"sudo apt install python3"

How to install Django:
Add it to the requirements.txt
"python3 -m pip install --upgrade pip"
"pip install -r requirements.txt"

#Lab 3 
For tests: 
With SQLite, in-memory database is used for testing, but I added a line to settings.py to make sure everything works well: 
'TEST': {'ENGINE': 'django.db.backends.sqlite3',} 
 
As my site is showing current time now, I ran a test to check that there is no problem with identifying the current time for system 
For Django unit tests Python module unittest is used. 
I use command 'python manage.py test tests' to run them, the goal is to see 'Ran 1 test in 0.001s OK'

For Github actions I used github website itself, and Jenkins was ran on localhost (more is specified in CI.md)

#Lab 4
I got familiar with Terraform, used Vargant for creating virtual box instance and also created an instance on AWS (more specified on TF.md)