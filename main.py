import socket
import json
import urllib.request

def cek_osint_domain(domain):
    print(f"\n[+] Memproses OSINT untuk: {domain}")
    print("=" * 40)
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"[!] IP Address : {ip_address}")
        url = f"http://ip-api.com/json/{ip_address}"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())
        if data['status'] == 'success':
            print(f"[!] Negara     : {data.get('country')}")
            print(f"[!] Kota       : {data.get('city')}")
            print(f"[!] ISP        : {data.get('isp')}")
        else:
            print("[-] Gagal mengambil data.")
    except Exception as e:
        print(f"[-] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    target = input("Masukkan domain (contoh: google.com): ")
    target = target.replace("https://", "").replace("http://", "").split("/")[0]
    cek_osint_domain(target)
  
