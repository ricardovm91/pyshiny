# Pyshiny

An easy to deploy Python API for Shiny apps using Flask.

## Initial Setup

To run this as smoothly as possible, you'll need Docker. 

* To install Docker on Windows and Mac follow this [link](https://www.docker.com/get-started).
* To install Docker on Ubuntu follow this [tutorial](https://docs.docker.com/install/linux/docker-ce/ubuntu/). 
* Create a Docker account [here](https://hub.docker.com/). This might not be mandatory but for sure will be useful for you at some point.

## Get started with Pyshiny

First of all, clone the repo, open your terminal, navigate to the **pyshiny** folder, and follow the next steps.

#### 1. Configure the env.py file.

This server is meant to have only server-to-server communication over **https** when deployed in production. In order to authenticate itself, the requesting server (a Shiny app in this case) needs to send a **parameter in the header named token** with a key that the Pyshiny server will validate. If you want to read abour how to send this data on the header on R, you can find that information [here](https://rdrr.io/cran/httr/man/add_headers.html).

Going back to the env.py file...

1. Go to your **/app** directory and rename the env.rename file to **env.py**
2. Create a secure token and fill the `token = ""` line with your new key. You can easily create one [here](https://randomkeygen.com/).
3. If you're using a database you can add the DB credentials to your file.
4. Feel free to add any other settings your server needs.

#### 2. Build and run the docker container

You may add or remove dependencies as you wish by modifying the *requirements.txt* file.

* Run `docker-compose build` to create the container.
* Run `docker-compose up -d` to activate the container (It will be kept alive since we're running it detached).
* Run `docker-compose stop` to deactivate the container.

#### 3. Enjoy

1. Go to your browser and type `localhost`. You should see a message saying **"Still Alive!"**. You're container is now running on port 80.
2. Go to Postman (or similar), send a GET or POST request to `localhost/myroute` with the token on the header and you should see **"Allow"** on your screen.

You now have a running REST server that you can use to add Python functionality to your Shiny App.

## Deploying on Heroku

Create a Heroku account and install the Heroku CLI ([Steps here](https://devcenter.heroku.com/articles/heroku-cli)).

Start by adding these lines to the end of the Dockerfile:
```
# Define our command to be run when launching the container
CMD gunicorn app:app --bind 0.0.0.0:$PORT --reload
```

Then go to the file *docker-compose.override.yml* and replace the content for this config:
```
version: '3.7'

services:
  web:
    command: gunicorn app:app --bind 0.0.0.0:$PORT --reload
    ports:
      - $PORT:$PORT
```

Then open your terminal and run:

```
heroku login
heroku container:login
```
Then create a new Heroku app and copy the name of the app.

`heroku create`

Push your Docker container to heroku.
`heroku container:push web --app {Your-App-Name}`

Release the container.
`heroku container:release web --app {Your-App-Name}`

Add Dynos to your Heroku app.
`heroku ps:scale web=1 --app {Your-App-Name}`

Test your app. You're all set!
`heroku open`

## Additional links

[Docker cheatsheet](https://gist.github.com/bradtraversy/89fad226dc058a41b596d586022a9bd3)

[Docker Compose cheatsheet](https://devhints.io/docker-compose)

