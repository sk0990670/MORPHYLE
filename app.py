from flask import Flask
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the name and username
    name = "Sujeet Kumar"
    username = subprocess.getoutput('whoami')

    # Get the server time in IST
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S.%f')

    # Get the top output
    top_output = subprocess.getoutput('top -b -n 1')

    # Format the output
    output = f"""
    Name: {name}<br>
    Username: {username}<br>
    Server Time (IST): {server_time}<br>
    <pre>{top_output}</pre>
    """

    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
