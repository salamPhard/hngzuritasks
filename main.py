from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# creating a api endpoint 2 GET Request Query using slack_name and track
@app.route('/hngtask1', methods=['GET'])
def get_user_data():
    slack_name = request.args.get('slack_name')
    current_day = datetime.now().strftime("%A")
    track = request.args.get('track')
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/salamPhard/hngzuritasks.git"
    github_repo_url = "https://github.com/salamPhard/hngzuritasks/blob/master/main.py"
    status_code = 200
    data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "track": track,
        "utc_time": utc_time,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": status_code
    }
    return jsonify(data)




if __name__ == '__main__':
    app.run(debug=True)
