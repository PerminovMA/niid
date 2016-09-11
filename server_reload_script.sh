#!/bin/bash

sudo service nginx restart
sudo uwsgi -y conf/uwsgi.yaml
