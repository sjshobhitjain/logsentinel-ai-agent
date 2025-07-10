# logsentinel-ai-agent
Anomaly detection agent using Isolation Forest

This is v2 of logsentinel-ai that updates A one-time script that loads a log file and runs anomaly detection using Isolation Forest to an AI agent that
- Watches logs live (like /var/log/syslog)
- Parses new lines as they are written
- Converts them into features
- Scores them using an Isolation Forest
- Flags & prints/logs alerts when anomalies are found


## 🚀 New: Real-Time AI Agent Mode

You can now run LogSentinel as a **live agent** that monitors logs continuously — just like lightweight endpoint detection (EDR/MDR) systems.

```bash
pip install -r requirements.txt

python src/agent.py
```

Watch the specified log file in real time (e.g., syslog, auth.log)
Parse new log entries on the fly
Extract AI-friendly features
Score using the trained Isolation Forest model
Print an alert if an anomaly is detected
