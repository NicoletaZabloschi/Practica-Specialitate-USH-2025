from collections import Counter

def analiza_alerte(log_file_path='data/alerts.log'):
    tipuri_alerte = []

    try:
        with open(log_file_path, 'r', encoding='utf-8') as f:
            for linie in f:
                if "Tip atac:" in linie:
                    start = linie.find("Tip atac:") + len("Tip atac:")
                    tip_alerta = linie[start:].strip()
                    if tip_alerta:
                        tipuri_alerte.append(tip_alerta)
    except FileNotFoundError:
        print("[ERROR] Fisierul de log nu a fost gasit.")
        return

    counter = Counter(tipuri_alerte)

    print("\nNumarul total de alerte pe fiecare tip:")
    if counter:
        for tip, nr in counter.items():
            print(f"{tip}: {nr}")
    else:
        print("Nu s-au gasit alerte în fisier.")
