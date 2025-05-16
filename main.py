import threading
import time
from agent.monitor import start_monitoring
from attacks.ddos_simulator import start_ddos
from attacks.spoofing_simulator import start_spoofing
from data.alerts import analiza_alerte
from sensors.temperature_sensor import run_sensor as run_temp_sensor
from sensors.humidity_sensor import run_sensor as run_humidity_sensor

def run_monitor():
    start_monitoring()

def main():
    # Pornește monitorizarea într-un thread separat
    monitor_thread = threading.Thread(target=run_monitor, daemon=True)
    monitor_thread.start()

    while True:
        print("\n=== Meniu principal ===")
        print("1. Simulare atac DDoS")
        print("2. Simulare atac Spoofing")
        print("3. Analiza alerte")
        print("4. Pornire senzor temperatura")
        print("5. Pornire senzor umiditate")
        print("6. Iesire")
        choice = input("Alege o optiune: ").strip()

        if choice == "1":
            print("[INFO] Pornire atac DDoS...")
            start_ddos()
        elif choice == "2":
            print("[INFO] Pornire atac Spoofing...")
            start_spoofing()
        elif choice == "3":
            analiza_alerte()
        elif choice == "4":
            print("[INFO] Simulare senzor temperatura...")
            threading.Thread(target=run_temp_sensor, daemon=True).start()
        elif choice == "5":
            print("[INFO] Simulare senzor umiditate...")
            threading.Thread(target=run_humidity_sensor, daemon=True).start()
        elif choice == "6":
            print("Iesire din aplicatie...")
            break
        else:
            print("Optiune invalida. Incearcă din nou.")

        time.sleep(1)

if __name__ == "__main__":
    main()
