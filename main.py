import requests
import threading

def webhook_spam(webhook_url, content, username=None, avatar_url=None):
    data = {"content": content}
    if username:
        data["username"] = username
    if avatar_url:
        data["avatar_url"] = avatar_url

    while True:
        try:
            response = requests.post(webhook_url, json=data)
            if response.status_code == 204:
                print(f"[+] 성공: {webhook_url.rsplit('/', 1)[-1][:15]}")
            else:
                print(f"[-] 실패 (상태 코드: {response.status_code})")
        except Exception as e:
            print(f"[!] 오류: {e}")

def start_spam(threads, webhook_url, content, username=None, avatar_url=None):
    for _ in range(threads):
        thread = threading.Thread(target=webhook_spam, args=(webhook_url, content, username, avatar_url), daemon=True)
        thread.start()
    
    while True:
        pass

username = "Discord"
avatar_url = "https://discord.com/assets/847541504914fd33810e70a0ea73177e.ico"
webhook_url = "https://discord.com/api/webhooks/xxxx/xxxxxxx"
message = "@everyone "
threads = 100

start_spam(threads, webhook_url, message, username, avatar_url)