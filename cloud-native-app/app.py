from flask import Flask, render_template, jsonify
import psutil

app = Flask(__name__)

def get_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=0.5),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent,
        "network": {
            "sent": round(psutil.net_io_counters().bytes_sent / (1024 * 1024), 2),
            "recv": round(psutil.net_io_counters().bytes_recv / (1024 * 1024), 2),
        }
    }

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/metrics")
def metrics():
    return jsonify(get_metrics())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
