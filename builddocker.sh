#!/usr/bin/bash
cd frontend/weather_buddy
npm rum build
cd -
sudo docker build . --tag weather_buddy