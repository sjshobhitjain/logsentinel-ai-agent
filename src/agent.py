import time
from pathlib import Path
from parser import parse_log_line
from features import extract_features
from model import LogAnomalyModel

LOG_FILE = "logs/sample_syslog.log"  # Replace with /var/log/syslog in real use

# Initialize and train the model using historical data
def initialize_model():
    parsed_logs = []
    with open(LOG_FILE, 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                parsed_logs.append(parsed)
    X = extract_features(parsed_logs)
    model = LogAnomalyModel()
    model.train(X)
    return model, parsed_logs

# Watch for new log lines in real time
def monitor_logs(model):
    with open(LOG_FILE, 'r') as f:
        f.seek(0, 2)  # Move to end of file

        while True:
            line = f.readline()
            if not line:
                time.sleep(0.5)
                continue

            parsed = parse_log_line(line)
            if not parsed:
                continue

            X_new = extract_features([parsed])
            prediction = model.predict(X_new)[0]
            if prediction == -1:
                print(f"⚠️ Anomaly detected: {parsed}")

if __name__ == "__main__":
    print("Initializing model from historical logs...")
    model, logs = initialize_model()
    print("Agent is now monitoring logs for anomalies...")
    monitor_logs(model)
