##Create image from Dockerfile
In pyshiny directory
`docker build -t pyshiny .`

##Create container with bind mount
`docker container run -d -p 80:80 -v /path/to/pyshiny/app:/app --name pyshinycont pyshiny`

##Exec with bash
`docker container exec -it pyshinycont bash` 

