# Pyshiny

An easy to deploy Python API for Shiny apps using Flask.

## Initial Setup

To run this as smoothly as possible, you'll need Docker. 

* To install Docker on Windows and Mac follow this [link](https://www.docker.com/get-started).
* To install Docker on Ubuntu follow this [tutorial](https://docs.docker.com/install/linux/docker-ce/ubuntu/). 
* Create a Docker account [here](https://hub.docker.com/). This might not be mandatory but for sure will be useful for you at some point.

## Get started with Pyshiny

First of all, clone the repo, open your terminal, navigate to the **pyshiny** folder, and follow the next steps.

#### 1. Create an image from the Dockerfile

In the Dockerfile you'll find that we're starting from a basic Python image and we're adding dependencies: 

* `Flask` for route management
* `gunicorn` for our web server
* `psycopg2` for PostgreSQL
* `pandas` for data wrangling

You may add or remove dependencies as you wish.

To create a new image run: `docker build -t pyshiny .` .

#### 2. Configure the env.py file.

This server is meant to have only server-to-server communication over **https**. In order to authenticate itself, the requesting server (a Shiny app in this case) needs to send a **parameter in the header named token** with a key that the Pyshiny server will validate. If you want to read abour how to send this data on the header, you can find that information [here](https://rdrr.io/cran/httr/man/add_headers.html).

Going back to the env.py file...

1. Go to your **/app** directory and rename the env.rename file to **env.py**
2. Create a secure token and fill the `token = ""` line with your new key. You can easily create one [here](https://randomkeygen.com/).
3. If you're using a database you can add the DB credentials to your file.
4. Feel free to add any other settings your server needs.
5. Create the container with a volume bind by running on the terminal:
* `docker container run -d -p 80:5000 -e PORT=5000 -v /path/to/pyshiny/app:/app --name pyshinycont pyshiny`
* **OR**  `docker container run -d -p 80:5000 -e PORT=5000 -v $(pwd)/app:/app --name pyshinycont pyshiny` (not sure if it works on a Windows machine).
6. After creating your container go to your browser and type `localhost`. You should see a message saying **"Still Alive!"**. You're container is now running on port 80.

You're all set now. Go to Postman (or similar), send a GET or POST request to `localhost/myroute` with the token on the header and you should see **"Allow"** on your screen.

You now have a running REST server that you can use to add Python functionality to your Shiny App. We hope to keep extending the repo with more stuff in the near future.

#### 3. Starting and stoping your server.
This is useful if it is your first time using Docker.

1. Stop the container by running on the terminal `docker stop pyshinycont`.
2. Start your container again by running `docker start pyshinycont -i` if you want to see the server's log or `docker start pyshinycont` if you want it to run on the background.

## Deploying on Heroku

Create a Heroku account and install the Heroku CLI ([Steps here](https://devcenter.heroku.com/articles/heroku-cli)).

Open your terminal and run:

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

