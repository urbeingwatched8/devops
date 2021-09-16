Lab1 - created the simplest Python web app using Django and Sqlite3. 
The Moscow time is showing and is updated with every refresh of the page (simple html&js). 
I followed the tutorial from Django documentation. The reason I chose Django was that I am familiar with it already. I also looked up the best tactics for showing the current time.

Some websites recommended Flask, but I decided to keep going with Django
For the databases, some of the things which were recommended were Postgres and MongoDB, but i went on with SQLite
HTML+JS are simple and popular for making sites.

How to install Python:
"sudo apt install python3"

How to install Django:
Add it to the requirements.txt
"python3 -m pip install --upgrade pip"
"pip install -r requirements.txt"

For creating 'blog' to make an HTML file:
"python manage.py makemigrations blog"
"python manage.py migrate blog"

LAB 3
My unit tests:
I decided to run a test which checks that the time on my app is precise.
I imported 'from django.test import TestCase' to run it and compared my way of reflecting & printing time to time from imported django timezone.

Best testing practices:
1. Use a controlled security environment for testing
2. Tests should be broken into small fractions
3. All tests should be reported and noted. 
4. Testing should be customized
5. Target operating model for testing should be developed.