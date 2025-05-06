# 🌥️ Cloud Native Monitor

A lightweight Flask-based system monitor with a web UI to display real-time **CPU**, **memory**, **disk**, and **network** metrics.

> Built for modern cloud-native environments with Docker support and a beautiful UI using Bootstrap and Chart.js.

---

## 📸 Dashboard Preview

![UI Preview](Screenshot)

---

## 🚀 Features

- Real-time monitoring of:
  - ✅ CPU usage
  - ✅ Memory consumption
  - ✅ Disk space usage
  - ✅ Network activity (sent/recv)
- Beautiful UI with [Bootstrap](https://getbootstrap.com/)
- Interactive charts via [Chart.js](https://www.chartjs.org/)
- Auto-refreshing stats every 2 seconds
- Docker-compatible for containerized deployments

---

## 🧰 Requirements

- Python 3.8+
- psutil
- Flask

Install with:

```bash
pip install -r requirements.txt
