import datetime
import pytz
from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def get_current_day():
    # Get the current day of the week
    day = datetime.datetime.now().strftime("%A")
    return day


def get_current_utc_time_with_timezone():
    # Get the current UTC time with timezone
    utc_time = datetime.datetime.now(
        pytz.timezone('UTC')).strftime("%Y-%m-%dT%H:%M:%SZ")
    return utc_time


def get_github_file_url():
    # Get the GitHub URL of the file being run
    github_file_url = "https://github.com/karanidenis/Zuri_projects/blob/main/endpoint.py"
    return github_file_url


def get_github_repo_url():
    # Get the GitHub URL of the full source code repo
    github_repo_url = "https://github.com/karanidenis/Zuri_projects/tree/main"
    return github_repo_url


@app.route('/endpoint', methods=['GET'])
# Endpoint
def endpoint():
    # Get the "slack_name" and "track" query parameters from the request
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    if slack_name is None or track is None:
        # If any of the parameters are missing, return a 400 Bad Request status
        return jsonify({"message": "Bad Request - Missing Parameters"}), 400

    current_day = get_current_day()
    utc_time = get_current_utc_time_with_timezone()
    github_file_url = get_github_file_url()
    github_repo_url = get_github_repo_url()
    status_code = 200
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }
    try:
        return jsonify(response_data)

    except Exception as e:
        status_code = 400
        print(jsonify({"message": "Error"}), 400)
        return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
