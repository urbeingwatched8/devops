I familiarized myself with provided materials, and this link was extremely useful.
https://github.com/black-rosary/loki-nginx

How to install promtail and loki:
1. 'wget https://raw.githubusercontent.com/grafana/loki/v2.3.0/cmd/loki/loki-local-config.yaml -O loki-config.yaml'

2. 'docker run -v $(pwd):/mnt/config -p 3100:3100 grafana/loki:2.3.0 -config.file=/mnt/config/loki-config.yaml'

3. 'wget https://raw.githubusercontent.com/grafana/loki/v2.3.0/clients/cmd/promtail/promtail-docker-config.yaml -O promtail-config.yaml'

4. 'docker run -v $(pwd):/mnt/config -v /var/log:/var/log grafana/promtail:2.3.0 -config.file=/mnt/config/promtail-config.yaml'

(but after using this kind of installation we need to stop the processes that started)

Best practices:
1. Be aware of Promtail (and other clients) dynamic labels
2. Use chunk_target_size (used in loki.yml)
3. It is important to configure caching
4. Label values should be always bounded
5. It is recommended for logs to be in increasing time order

These are available containers and visible labels:
![alt text](https://github.com/urbeingwatched8/devops/blob/8f1d0a15b5da66fd6c25f88366c004acb1c85b75/monitoring/pictures/photo_2021-09-13_13-05-58.jpg?raw=true)

This is how I see logs now:
![alt text](https://github.com/urbeingwatched8/devops/blob/8f1d0a15b5da66fd6c25f88366c004acb1c85b75/monitoring/pictures/photo_2021-09-13_13-05-58.jpg?raw=true)