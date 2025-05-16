import streamlit as st
import threading
import time
import queue
from attacks.ddos_simulator import start_ddos
from attacks.spoofing_simulator import start_spoofing
from data.alerts import analiza_alerte
from sensors.temperature_sensor import run_sensor as run_temperature_sensor
from sensors.humidity_sensor import run_sensor as run_humidity_sensor
from utils.logger import set_log_queue  # importă funcția de setare coadă

log_queue = queue.Queue()

set_log_queue(log_queue)

if 'log_messages' not in st.session_state:
    st.session_state.log_messages = []

def log(msg):
    log_queue.put(msg)

def update_logs_from_queue():
    while not log_queue.empty():
        st.session_state.log_messages.append(log_queue.get())
    if len(st.session_state.log_messages) > 100:
        st.session_state.log_messages = st.session_state.log_messages[-100:]

def run_ddos(log):
    log("[INFO] Pornire atac DDoS...")
    start_ddos(log_func=log)
    log("[INFO] Atac DDoS terminat.")

def run_spoofing(log):
    log("[INFO] Pornire atac Spoofing...")
    start_spoofing(log_func=log)
    log("[INFO] Atac Spoofing terminat.")

def run_temperature(log):
    log("[INFO] Pornire senzor temperatura...")
    run_temperature_sensor(log)
    log("[INFO] Senzor temperatura a trimis 5 valori și s-a oprit.")

def run_humidity(log):
    log("[INFO] Pornire senzor umiditate...")
    run_humidity_sensor(log)
    log("[INFO] Senzor umiditate a trimis 5 valori și s-a oprit.")

def run_analysis():
    log("[INFO] Pornire analiza alerte...")
    output = analiza_alerte()
    log(output)

st.title("Sistem Monitorizare Atacuri & Senzori")

for key in ['thread_ddos', 'thread_spoofing', 'thread_temp', 'thread_humidity']:
    if key not in st.session_state:
        st.session_state[key] = None

col1, col2 = st.columns(2)

with col1:
    if st.button("Simulare atac DDoS"):
        if st.session_state.thread_ddos is None or not st.session_state.thread_ddos.is_alive():
            t = threading.Thread(target=run_ddos, args=(log,), daemon=True)
            st.session_state.thread_ddos = t
            t.start()
        else:
            st.warning("Atac DDoS este deja în desfășurare.")

    if st.button("Simulare atac Spoofing"):
        if st.session_state.thread_spoofing is None or not st.session_state.thread_spoofing.is_alive():
            t = threading.Thread(target=run_spoofing,args=(log,), daemon=True)
            st.session_state.thread_spoofing = t
            t.start()
        else:
            st.warning("Atac Spoofing este deja în desfășurare.")

with col2:
    if st.button("Pornire senzor temperatura"):
        if st.session_state.thread_temp is None or not st.session_state.thread_temp.is_alive():
            t = threading.Thread(target=run_temperature, args=(log,), daemon=True)
            st.session_state.thread_temp = t
            t.start()
        else:
            st.warning("Senzor temperatura este deja pornit.")

    if st.button("Pornire senzor umiditate"):
        if st.session_state.thread_humidity is None or not st.session_state.thread_humidity.is_alive():
            t = threading.Thread(target=run_humidity, args=(log,), daemon=True)
            st.session_state.thread_humidity = t
            t.start()
        else:
            st.warning("Senzor umiditate este deja pornit.")

if st.button("Analiza alerte"):
    run_analysis()

st.subheader("Log activitati")

log_area = st.empty()

def update_logs():
    update_logs_from_queue()
    log_area.text("\n".join(st.session_state.log_messages[-30:]))

update_logs()

if 'last_refresh' not in st.session_state:
    st.session_state.last_refresh = time.time()

if time.time() - st.session_state.last_refresh > 1:
    st.session_state.last_refresh = time.time()
    st.rerun()
