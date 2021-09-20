as command line:

kubectl get pods,svc
NAME                                       READY   STATUS             RESTARTS        AGE
pod/kubernetes-bootcamp-7b6c8cb486-jzbct   1/1     Running            0     		15m

NAME                          TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
service/kubernetes            ClusterIP   10.96.0.1        <none>        443/TCP          23m
service/kubernetes-bootcamp   LoadBalancer   10.111.38.197   10.111.38.197   8080:32602/TCP   19s

as files:
urbenata8@urbenata8-N552VW:~/Downloads/devopslab1/k8s$ kubectl apply -f ./
deployment.apps/web created
service/web created
urbenata8@urbenata8-N552VW:~/Downloads/devopslab1/k8s$ kubectl get pods,svc
NAME                       READY   STATUS    RESTARTS   AGE
pod/web-6d46b5b859-4zw2c   1/1     Running   0          4s
pod/web-6d46b5b859-7v27l   1/1     Running   0          4s
pod/web-6d46b5b859-kkgnz   1/1     Running   0          4s

NAME                 TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)          AGE
service/kubernetes   ClusterIP      10.96.0.1        <none>           443/TCP          14h
service/web          LoadBalancer   10.102.255.131   10.102.255.131   8000:30130/TCP   4s

