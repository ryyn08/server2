import time, subprocess, os, sys
from config import proxies

COLORS = {
    "Canada": "\033[94m",
    "Singapore": "\033[92m",
    "USA": "\033[93m",
    "India": "\033[95m",
    "RESET": "\033[0m",
    "RED": "\033[91m"
}

def clear_screen():
    # Perintah untuk membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ms(ip):
    try:
        # Menggunakan -c 1 dan timeout 1 detik agar lebih responsif (real-time)
        res = subprocess.check_output(f"ping -c 1 -W 1 {ip}", shell=True).decode()
        return float(res.split("time=")[1].split(" ms")[0])
    except: return 999.0

def monitor_loop(target_name=None):
    """Fungsi loop utama agar tetap real-time"""
    while True:
        clear_screen()
        print(f"--- LIVE SERVER MONITOR (ryyn08) ---")
        print(f"Tekan 'Ctrl + C' untuk berhenti ke menu\n")
        
        try:
            if target_name: # Mode 1 Server
                servers = {target_name: proxies[target_name]}
            else: # Mode All
                servers = proxies
            
            for name, ip in servers.items():
                ms = get_ms(ip)
                status = f"{COLORS['RED']}DISCONNECT{COLORS['RESET']}" if ms >= 200 else "CONNECTED"
                color = COLORS.get(name, COLORS['RESET'])
                print(f"{color}[{name}]{COLORS['RESET']} | IP: {ip} | Latency: {ms}ms | Status: {status}")
            
            time.sleep(1) # Update per 1 detik
        except KeyboardInterrupt:
            break # Kembali ke menu jika user menekan Ctrl+C

def main():
    while True:
        print("\n--- MENU MONITORING ---")
        print("1. All Servers (Real-time)")
        print("2. Pilih 1 Server (Real-time)")
        print("0. Keluar")
        choice = input("Pilih menu: ")

        if choice == "1":
            monitor_loop()
        elif choice == "2":
            keys = list(proxies.keys())
            for i, name in enumerate(keys): print(f"{i+1}. {name}")
            idx = int(input("Pilih nomor: ")) - 1
            if 0 <= idx < len(keys):
                monitor_loop(keys[idx])
        elif choice == "0":
            sys.exit()

if __name__ == "__main__":
    main()
