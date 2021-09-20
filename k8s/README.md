Lab 9
Kubernetes

How to install Kubernetes:
1. 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"'
2. 'curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"'
3. 'echo "$(<kubectl.sha256) kubectl" | sha256sum --check'
4. 'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl'

Basically, I was following the tutorials from given links. Kubernetes interactive tutorial was the most helpful.
To make load balancer work better (external IP) I used command 'minikube tunnel' in another terminal.

Result from 'kubectl get pods,svc' after steps 1-5:
![alt text](https://github.com/urbeingwatched8/devops/blob/abb2319cf2bd57883f8f045f2ee3bdccd59bd369/k8s/screenshots/%D0%91%D0%B5%D0%B7%D1%8B%D0%BCffds%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9.png?raw=true)

For steps 7-9, I faced an issue with connecting to DB so I worked with 'kompose' (which helped me to translate docker-compose.yml to kubernetes resources). I got many different files but I compiled them into 2 (deployment.yml, service.yml) and everything worked perfectly.
The result with 3 replicas:
![alt text](https://github.com/urbeingwatched8/devops/blob/abb2319cf2bd57883f8f045f2ee3bdccd59bd369/k8s/screenshots/photo_2021-09-20_13-05-08.jpg?raw=true)