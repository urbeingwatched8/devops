Github actions:

Github actions allow to build, test and publish the project (now all stages work fine).

No installations needed, I worked on Github.com with the files that I already pushed. 

A good tutorial that I followed:https://docs.github.com/en/actions/quickstart (basically, after that I could see that my tests work in Actiona)

Best Practices:
1. Keep actions minimal.
2. Make sure that secrets aren't public (hardcoded).
3. Limit environment variables.
4. Don't install unnecessary dependencies.
5. Make sure that every repository contains a workflow.

After seeing simplest actions working, I edited the github-actions-demo.yml file according to Docker documentation to check that everything is fine with Docker. (https://docs.docker.com/ci-cd/github-actions/)

After docker bulidx is set up, the image can be pushed, and we can use cache later to save some time.

Jenkins:

The best practices are:

1.Keep the Jenkins secure.

2.Set up a different project for each branch.

3.Do backup (by using plugins, for example).

4.Create a scalable pipeline.

5.Avoid resource collisions for parallel running jobs.

I took the security issue too seriously and couldn't even login as admin at some point.

Jenkins needs Java to run:'sudo apt install openjdk-11-jdk'
The jenkins installation itself: 'wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > \
    /etc/apt/sources.list.d/jenkins.list'
sudo apt-get install jenkins' 

More info, if needed, can be found on Jenkins documentation. https://www.jenkins.io/doc/book/installing/linux/#debianubuntu

I followed this tutorial - https://www.jenkins.io/doc/tutorials/create-a-pipeline-in-blue-ocean/

After accessing localhost:8000, I did everything according to the file with homework task.
Everything worked fine for me and I can provide screenshots on telegram if needed.