import time, subprocess, sys
from config import proxies

# ANSI Color Codes
COLORS = {
    "Canada": "\033[94m",      # Biru
    "Singapore": "\033[92m",   # Hijau
    "USA, Los Angeles": "\033[93m", # Kuning
    "India, Hyderabad": "\033[95m", # Magenta
    "RESET": "\033[0m",
    "RED": "\033[91m"
}

def get_ms(ip):
    try:
        res = subprocess.check_output(f"ping -c 1 -W 2 {ip}", shell=True).decode()
        return float(res.split("time=")[1].split(" ms")[0])
    except: return 999.0

def display_server(name, ip, mode="all"):
    ms = get_ms(ip)
    status = f"{COLORS['RED']}DISCONNECT{COLORS['RESET']}" if ms >= 200 else "CONNECTED"
    color = COLORS.get(name, COLORS['RESET'])
    
    print(f"{color}[{name}]{COLORS['RESET']} | IP: {ip} | Latency: {ms}ms | Status: {status}")

def main():
    while True:
        print("\n--- SERVER PROXY RIN ---")
        print("1. All Servers Log")
        print("2. Select Specific Server")
        print("0. Exit")
        choice = input("Pilih menu: ")

        if choice == "1":
            print("\n--- Monitoring All Servers ---")
            for name, ip in proxies.items():
                display_server(name, ip)
        
        elif choice == "2":
            print("\nList Server:")
            keys = list(proxies.keys())
            for i, name in enumerate(keys): print(f"{i+1}. {name}")
            idx = int(input("Pilih nomor: ")) - 1
            if 0 <= idx < len(keys):
                name = keys[idx]
                display_server(name, proxies[name])
            else: print("Pilihan tidak valid!")
            
        elif choice == "0": sys.exit()
        
        time.sleep(2)

if __name__ == "__main__":
    main()
