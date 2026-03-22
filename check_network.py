import socket
import requests
import platform

def get_network_info():
    print(f"--- 系統資訊 ---")
    print(f"作業系統: {platform.system()} {platform.release()}")
    
    print(f"\n--- 網路測試 ---")
    # 測試外部連線與獲取公網 IP
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        ip = response.json()['ip']
        print(f"你的公網 IP 是: {ip}")
    except Exception as e:
        print(f"無法取得公網 IP: {e}")

    # 取得本機主機名稱
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"本機名稱: {hostname}")
    print(f"本機 IP (Internal): {local_ip}")

if __name__ == "__main__":
    get_network_info()
