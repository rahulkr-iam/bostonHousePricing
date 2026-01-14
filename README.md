# bostonHousePricing


# Software and tools requirement

1. [Github Account](https://github.com)
2. [Heroku Account](https://heroku.com)
3. [Vs Code IDE](https://code.visualstudio.com/)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)



Create a new environment for the project
```
conda create -p venv python==3.7 -y
```


Usually any app we deploy or heroku,
A procFile specify some commands that needs to be exicuted by the app as soon as it starts.
Procfile  is basically for indicating/ giving a kind of command to the heroku instance that,
at the start of entire app, what commands need to run. 

Command are related to GUnicorn, Green Unicorn is basically for python http server or WSGI application, it allows us to run python programs concurrently by running multiple processes.