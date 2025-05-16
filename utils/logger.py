def log_alert(message: str, attack_type: str = None):
    try:
        with open("data/alerts.log", "a", encoding="utf-8") as file:
            if attack_type:
                file.write(f"Tip atac: {attack_type} - {message}\n")
                print(f"[ALERT LOG] Tip atac: {attack_type} - {message}")
            else:
                file.write(message + "\n")
                print(f"[ALERT LOG] {message}")
    except Exception as e:
        print(f"[ERROR] Nu s-a putut scrie in fisier: {e}")
