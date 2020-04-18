#!/bin/bash
docker build -t opencart_tests .
docker run opencart_tests --url=http://192.168.1.5
docker system prune -af
