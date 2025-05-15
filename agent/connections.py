import psutil
from utils.logger import log_alert

CONNECTION_THRESHOLD = 100
UDP_PACKET_THRESHOLD = 50

def monitor_connections():
    connections = psutil.net_connections()
    active_tcp = [c for c in connections if c.status == 'ESTABLISHED' and c.type == psutil.SOCK_STREAM]

    # Nr. conexiuni TCP
    if len(active_tcp) > CONNECTION_THRESHOLD:
        log_alert(f"Numar mare de conexiuni TCP active detectat: {len(active_tcp)}")

    # Monitorizare trafic UDP activ
    net_io = psutil.net_io_counters(pernic=False)
    udp_packets_sent = net_io.packets_sent

    # Alerta
    if udp_packets_sent > UDP_PACKET_THRESHOLD:
        log_alert(f"Numar mare de pachete UDP trimise: {udp_packets_sent}")

    print(f"[INFO] Conexiuni TCP active: {len(active_tcp)}, Pachete trimise total: {udp_packets_sent}")
