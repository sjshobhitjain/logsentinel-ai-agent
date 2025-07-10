import hashlib

def hash_text(text):
    return int(hashlib.sha1(text.encode()).hexdigest(), 16) % (10**8)

def extract_features(parsed_logs):
    features = []
    for log in parsed_logs:
        features.append([
            hash_text(log["service"]),
            len(log["message"])
        ])
    return features
