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
        return "[ERROR] Fisierul de log nu a fost gasit."

    counter = Counter(tipuri_alerte)

    if counter:
        rezultat = "\nNumarul total de alerte pe fiecare tip:\n"
        for tip, nr in counter.items():
            rezultat += f"{tip}: {nr}\n"
    else:
        rezultat = "Nu s-au gasit alerte în fisier."

    return rezultat
