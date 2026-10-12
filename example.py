import time
import random
from pypresence import Presence

CLIENT_ID = "1553595070161231972"


LARGE_IMAGE_KEY = "icon"
LARGE_IMAGE_TEXT = "Grand Theft Auto VI"
SMALL_IMAGE_KEY = "gta6"
SMALL_IMAGE_TEXT = "fake"


STATUS_LIST = [
    {
        "details": "Free Roaming in Vice City ",
        "state": "Cruising down Ocean Drive",
        "small_text": "Radio: Vice City FM "
    },
    {
        "details": "Wanted Level: ⭐️⭐️⭐️⭐️",
        "state": "Evading Police ",
        "small_text": "High Speed Chase!"
    },
    {
        "details": "Planning Heist ",
        "state": "In Safehouse",
        "small_text": "Preparing for the big job"
    },
    {
        "details": "Chilling at the Beach ",
        "state": "Watching the Sunset",
        "small_text": "Vibing in Miami style"
    },
    {
        "details": "Flying Helicopter ",
        "state": "Over Vice City Skyline",
        "small_text": "Radio: Wave 103 "
    }
]

RPC = Presence(CLIENT_ID)
RPC.connect()

start_time = time.time()

print("🚗 Starting GTA6 Full Custom RPC...")

try:
    while True:
        
        current_status = random.choice(STATUS_LIST)
        
       
        current_players = random.randint(1, 64)
        
        RPC.update(
            details=current_status["details"],
            state=current_status["state"],
            start=int(start_time),
            large_image=LARGE_IMAGE_KEY,
            large_text=LARGE_IMAGE_TEXT,
            small_image=SMALL_IMAGE_KEY,
            small_text=current_status["small_text"],
            party_size=[current_players, 64],  
            buttons=[
                {
                    "label": "Rockstar Games Official",
                    "url": "https://www.rockstargames.com/",
                }
            ],
        )
        print(f"✨ Status: {current_status['details']} | Lobby: ({current_players}/64)")
        
        
        time.sleep(500)

except KeyboardInterrupt:
    print("Stopped RPC. See ya!")
