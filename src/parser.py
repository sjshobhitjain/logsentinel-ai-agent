import re

def parse_log_line(line):
    match = re.match(r'(\w+ \d+ \d+:\d+:\d+)\s+(\S+)\s+(\S+)\[(\d+)\]:\s+(.*)', line)
    if match:
        timestamp, hostname, service, pid, message = match.groups()
        return {
            "timestamp": timestamp,
            "hostname": hostname,
            "service": f"{service}[{pid}]",
            "message": message
        }
    return None
