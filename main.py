import json
import time
from pypresence import Presence

def load_config():
    with open("config.json", "r", encoding="utf-8") as f:
        return json.load(f)

def run():
    config = load_config()
    client_id = config.get("client_id")
    
    rpc = Presence(client_id)
    rpc.connect()
    print("[+] Connected to Discord RPC successfully!")

    start_time = int(time.time())

    while True:
        rpc.update(
            details=config.get("details"),
            state=config.get("state"),
            large_image=config.get("large_image"),
            large_text=config.get("large_text"),
            small_image=config.get("small_image"),
            small_text=config.get("small_text"),
            start=start_time,
            buttons=config.get("buttons")
        )
        time.sleep(15)

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\n[-] RPC disconnected.")
