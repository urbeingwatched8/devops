Lab 8

After reading provided materials, I configured Prometheus still following this example: https://github.com/black-rosary/loki-nginx . 

Most things which were provided in files related to Prometheus worked completely fine. 

Things like http://localhost:9090/targets , http://localhost:9090/metrics and http://localhost:3100/metrics worked:
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_22-20-06.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_20-16-12.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_18-17-04.jpg?raw=true)

Logs from Prometheus image:
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_18-05-38.jpg?raw=true)

Dashboards worked fine after adding Prometheus to Data Collectors:

Loki2.0 Global Metrics:
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-14-40.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-31-46.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-32-15.jpg?raw=true)

Prometheus 2.0 Overview:
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-21-09.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-21-28.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-21-45.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-22-36.jpg?raw=true)
![alt text](https://github.com/urbeingwatched8/devops/blob/e4678cea2b92bc243dc886661096c9263cd9e1c5/monitoring/pictures/photo_2021-09-13_19-23-08.jpg?raw=true)

For log rotation and mem limits I edited the docker-compose.yaml file in this folder. This part seems to work correctly as well.
This helped me:
https://medium.com/@Quigley_Ja/rotating-docker-logs-keeping-your-overlay-folder-small-40cfa2155412
