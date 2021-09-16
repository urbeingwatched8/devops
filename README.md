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
UNIT TESTS: 
With SQLite, in-memory database is used for testing, but I added a line to settings.py to make sure everything works well: 
'TEST': {'ENGINE': 'django.db.backends.sqlite3',} 
 
As my site is showing current time now, I ran a test to check that there is no problem with identifying the current time for system 
For Django unit tests Python module unittest is used. 
I use command 'python manage.py test tests' to run them, the goal is to see 'Ran 1 test in 0.001s OK'

For Github actions I used github website itself. The action has 3 stages, test, build and push. To save time, we use cache for building: build stage without cache takes 1 min 53 sec, and with cache it takes 28 seconds. The status badge changes with some time delay, but still works fine.
Jenkins was ran on localhost (more is specified in CI.md)

#Lab 4
I got familiar with Terraform, used Vargant for creating virtual box instance and also created an instance on AWS (more specified on TF.md)

#Lab 5 
Ansible installation:

1.'sudo python get-pip.py'

2. 'sudo python -m pip install ansible'

Docker role created after analysing this: https://github.com/geerlingguy/ansible-role-docker

THERE ARE MORE FOLDERS IN /roles/docker and /roles/app because they were created automatically! please look at the necessary folders only

#Lab 6
How to install Ansible-Lint:

'pip install ansible-lint'

Mostly followe https://docs.ansible.com/ansible/2.5/modules, avoiding shell and command modules as mentioned