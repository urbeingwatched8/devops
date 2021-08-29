#Lab1 
Created the simplest Python web app using Django and Sqlite3. 
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

#Lab 3
For tests:
It is important to rely on secure environment, and local DB seems to be a great choice for that. Also, tests themselves shouldn't be too big. Keeping the test code clean is just as important. (https://devops.com/13-best-practices-successful-software-testing-projects/)
