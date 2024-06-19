import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    alert_message = None
    if cpu_usage > 80 or memory_usage > 80:
        alert_message = "High CPU or Memory Detected, scale up!!!"
    return render_template("index.html", cpu_usage=cpu_usage, memory_usage=memory_usage, alert_message=alert_message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded=True)
