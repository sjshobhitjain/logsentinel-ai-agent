# logsentinel-ai-agent
Anomaly detection agent using Isolation Forest

This is v2 of logsentinel-ai that updates A one-time script that loads a log file and runs anomaly detection using Isolation Forest to an AI agent that
- Watches logs live (like /var/log/syslog)
- Parses new lines as they are written
- Converts them into features
- Scores them using an Isolation Forest
- Flags & prints/logs alerts when anomalies are found


