# Create and host an endpoint using any programming language of your choice.
# The endpoint should take two GET request query parameters and return specific information in JSON format.Requirements
# The information required includes:

#     Slack name
#     Current day of the week
#     Current UTC time (with validation of +/-2)
#     Track
#     The GitHub URL of the file being run
#     The GitHub URL of the full source code.
#     A  Status Code of Success

# JSON

#     {
#       "slack_name": "example_name",
#       "current_day": "Monday",
#       "utc_time": "2023-08-21T15:04:05Z",
#       "track": "backend",
#       "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
#       "github_repo_url": "https://github.com/username/repo",
#       “status_code”: 200
#     }


import requests
import json
import datetime
import time
import os
import sys
import re
import pytz
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

# Get the current day of the week
def get_current_day():
    day = datetime.datetime.now().strftime("%A")
    return day

# Get the current UTC time
def get_current_utc_time():
    utc_time = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    return utc_time

# Get the current UTC time with timezone    
def get_current_utc_time_with_timezone():
    utc_time = datetime.datetime.now(pytz.timezone('UTC')).strftime("%Y-%m-%dT%H:%M:%SZ")
    return utc_time

# Track
def get_track():
    track = "backend"
    return track

# Get the GitHub URL of the file being run
def get_github_file_url():
    github_file_url = ""
    return github_file_url

# Get the GitHub URL of the full source code
def get_github_repo_url():
    github_repo_url = ""
    return github_repo_url
    
# Get the status code
def get_status_code():
    status_code = 200
    return status_code

# Get the slack name
def get_slack_name():
    slack_name = ""
    return slack_name
    

# Endpoint
@app.route('/endpoint', methods=['GET'])
def endpoint():
    slack_name = get_slack_name()
    current_day = get_current_day()
    utc_time = get_current_utc_time_with_timezone()
    track = get_track()
    github_file_url = get_github_file_url()
    github_repo_url = get_github_repo_url()
    status_code = get_status_code()
    return jsonify(slack_name=slack_name, current_day=current_day, utc_time=utc_time, track=track, github_file_url=github_file_url, github_repo_url=github_repo_url, status_code=status_code)