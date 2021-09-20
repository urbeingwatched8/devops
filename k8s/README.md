Lab 9
Kubernetes

How to install kubectl:
1. 'curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"'
2. 'curl -LO "https://dl.k8s.io/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl.sha256"'
3. 'echo "$(<kubectl.sha256) kubectl" | sha256sum --check'
4. 'sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl'

How to install minikube:
1. 'curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64'
2. 'sudo install minikube-linux-amd64 /usr/local/bin/minikube'

Basically, I was following the tutorials from given links. Kubernetes interactive tutorial was the most helpful.
To make load balancer work better (external IP) I used command 'minikube tunnel' in another terminal.

Result from 'kubectl get pods,svc' after steps 1-5:
![alt text](https://github.com/urbeingwatched8/devops/blob/abb2319cf2bd57883f8f045f2ee3bdccd59bd369/k8s/screenshots/%D0%91%D0%B5%D0%B7%D1%8B%D0%BCffds%D1%8F%D0%BD%D0%BD%D1%8B%D0%B9.png?raw=true)

For steps 7-9, I faced an issue with connecting to DB so I worked with 'kompose' (which helped me to translate docker-compose.yml to kubernetes resources). I got many different files but I compiled them into 2 (deployment.yml, service.yml) and everything worked perfectly.
The result with 3 replicas:
![alt text](https://github.com/urbeingwatched8/devops/blob/abb2319cf2bd57883f8f045f2ee3bdccd59bd369/k8s/screenshots/photo_2021-09-20_13-05-08.jpg?raw=true)

Lab 10
Helm

How to install:
1. 'curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3'
2. 'chmod 700 get_helm.sh'
3. './get_helm.sh'

Once again, I mostly followed tutorials from given links. But of course a couple of things had to be edited after getting templates by running 'helm create your-app'.  
I took a look at minikube dashboard, but I still couldn't fix anything related to to livenessProbe and readinessProbe, so I commented them. Once again, I used 'minikube tunnel' for external IP.

To install Helm chart:  
'helm install your-app1 ./your-app-0.1.0.tgz'

Result from 'minikube service your-app1':
![alt text](https://github.com/urbeingwatched8/devops/blob/11b193655ad4a1410890aad1973ea52be3e909dd/k8s/screenshots/photo_2021-09-20_18-55-27.jpg?raw=true)
Result from ' kubectl get pods,svc':
![alt text](https://github.com/urbeingwatched8/devops/blob/11b193655ad4a1410890aad1973ea52be3e909dd/k8s/screenshots/photo_2021-09-20_19-23-05.jpg?raw=true)