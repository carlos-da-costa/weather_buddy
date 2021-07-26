# weather_buddy

To run in docker:

First build the image
```
    chmod +x builddocker.sh
    ./builddocker.sh
```

Now you can run:
```
    chmod +x rundocker.sh
    ./rundocker.sh
```
If run successfully, the app addres will be displayed on terminal.

To run locally, first create a virtual environment 
(I like virtualenv wrapper)
```
    mkvirtualenv weather_buddy
```

Then install packages
```
    pip install -r requirements.txt
```

And also build the frontend

```
    cd frontend/weather_buddy
    npm rum build
```

Create a .env with configurations
Remember to set up the openweathermap API inside this file
```
    cp .env-sample .env
```

Now you can run it with 
```
    flask run
```
    