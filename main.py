import threading
import time
from agent.monitor import start_monitoring
from attacks.ddos_simulator import start_ddos
from attacks.spoofing_simulator import start_spoofing
from data.alerts import analiza_alerte

def run_monitor():
    start_monitoring()

def main():
    monitor_thread = threading.Thread(target=run_monitor, daemon=True)
    monitor_thread.start()

    while True:
        print("\n=== Meniu principal ===")
        print("1. Simulare atac DDoS")
        print("2. Simulare atac Spoofing")
        print("3. Analiza alerte")
        print("4. Iesire")
        choice = input("Alege o opțiune: ").strip()

        if choice == "1":
            print("[INFO] Pornire atac DDoS...")
            start_ddos()
        elif choice == "2":
            print("[INFO] Pornire atac Spoofing...")
            start_spoofing()
        elif choice == "3":
            analiza_alerte()
        elif choice == "4":
            print("Iesire din aplicatie...")
            break
        else:
            print("Optiune invalida. Incearca din nou.")

        time.sleep(1)

if __name__ == "__main__":
    main()
