# data/data_analysis.py

from collections import Counter
import re

LOG_FILE = "data/alerts.log"

def parse_alerts():
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    alerts = []
    for line in lines:
        match = re.search(r"\[ALERT LOG\] (.+)", line)
        if match:
            alerts.append(match.group(1).strip())
    return alerts

def count_alert_types(alerts):
    return Counter(alerts)

def main():
    alerts = parse_alerts()
    alert_counts = count_alert_types(alerts)

    print(f"Numar total alerte: {len(alerts)}\n")
    print("Numarul total de alerte pe fiecare tip:")
    for alert_type, count in alert_counts.items():
        print(f"  - {alert_type}: {count}")

if __name__ == "__main__":
    main()
