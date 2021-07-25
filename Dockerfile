# syntax=docker/dockerfile:1

FROM nikolaik/python-nodejs:latest

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

# WORKDIR /app/frontend/weather_buddy

# CMD [ "npm", "run", "build"]

WORKDIR /app

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000"]

EXPOSE 5000
