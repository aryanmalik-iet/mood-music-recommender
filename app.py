from flask import Flask, render_template, request
import random

app = Flask(__name__)

mood_data = {
    "hindi": {
        "happy": {
            "songs": [
                "https://youtu.be/nJZcbidTutE?si=o35hUyUpBjsSUdkB",  
                "https://youtu.be/qpIdoaaPa6U?si=Kc61EWbHJZZJAhdf", 
                "https://youtu.be/jCEdTq3j-0U?si=zvKKonwNabgw5E4t",  
                "https://youtu.be/41iEgelUUzM?si=cY0JBUQXarjBHIe_"    
            ],
            "tip": ""
        },
        "sad": {
            "songs": [
                "https://youtu.be/lBvbNxiVmZA?si=hqMnGCKsJZJWVgkE",  
                "https://youtu.be/sVRwZEkXepg?si=D7ZigJ442gShacvW", 
                "https://youtu.be/1poXN3jF3Bw?si=HcoB6e8eKHt7JUN-", 
                "https://youtu.be/p9nYTT8KGeM?si=RQiRNgTLeY_Vfkqq"   
            ],
            "tip": ""
        },
        "romantic": {
            "songs": [
                "https://youtu.be/RazuWp5kSHk?si=5vxafKPvFUI_DeOT",  
                "https://youtu.be/-8C_2BBVWk8?si=U3um0fPUOF78H7IB", 
                "https://youtu.be/gvyUuxdRdR4?si=UBM2vRzi-JtxXsep",  
                "https://youtu.be/gvyUuxdRdR4?si=UBM2vRzi-JtxXsep"   
            ],
            "tip": ""
        },
        "energetic": {
            "songs": [
                "https://youtu.be/HoCwa6gnmM0?si=2K7oXNmNlXn3jQ71", 
                "https://youtu.be/abiL84EAWSY?si=D1IVnvi-zpOyNsN9",  
                "https://youtu.be/puKD3nkB1h4?si=eJAk4bv7VqUR0BPL",  
                "https://youtu.be/IjBAgWKW12Y?si=4od6_AScIcP3_Obu"   
            ],
            "tip": ""
        },
        "calm": {
            "songs": [
                "https://youtu.be/fSS_R91Nimw?si=YwdT03Y5DZqGhAVK", 
                "https://youtu.be/uVTdmJIcjtQ?si=72iCHVuJoMMj-PRD",  
                "https://youtu.be/JHUrRSBtUNE?si=bfSshxrOaaadVETM",  
                "https://youtu.be/sK7riqg2mr4?si=VjBxK1x6MDQ-dLmn"   
            ],
            "tip": ""
        }
    },

    "punjabi": {
        "happy": {
            "songs": [
                "https://youtu.be/PjTU0DmBWiU?si=mW6Ubli4VAZEUclO",  
                "https://youtu.be/Q-GOFPM01d0?si=BaFkEevY58_LaaNe",  
                "https://youtu.be/n3mJ9b6l33E?si=eyMveD-UrTrUvTNK", 
                "https://youtu.be/qgbvMJsz1Rk?si=_v4RevjIZTFz8yfz"  
            ],
            "tip": ""
        },
        "sad": {
            "songs": [
                "https://youtu.be/jynMDYYFB9I?si=4UoEoBQUQ337kHjC",  
                "https://youtu.be/QHJstKwI0Ic?si=0laHUPNjE3aR1ppX",  
                "https://youtu.be/enQuoRciccM?si=ZipmWT7XrNA_kHvc",  
                "https://youtu.be/Wd6TufgP3qs?si=zZ4u917V3_sGfMNs"  
            ],
            "tip": ""
        },
        "romantic": {
            "songs": [
                "https://youtu.be/X1xub3f7ubY?si=SvLrfJqwATz22kDF",  
                "https://youtu.be/_RywJ_FJ_3U?si=oQ7NI3l8dBZnOC8b",  
                "https://youtu.be/9udS0mpi1L4?si=yRlYZShcD85gKF6Q",  
                "https://youtu.be/jn77BhLMGc8?si=WXbGCRD0bOVyvFMh"   
            ],
            "tip": ""
        },
        "energetic": {
            "songs": [
                "https://youtu.be/RLhuPD2ASKE?si=v7DgBlFwqa6a5IYM",  
                "https://youtu.be/tpFljbJxZiw?si=eIGBvGcXCiLZ5sJT", 
                "https://youtu.be/GgmFC8y8q3k?si=4CBeKQRRQ74hGDqv",  
                "https://youtu.be/6xoB4ZiKKn0?si=gcMhr1bVOStz7_SJ"   
            ],
            "tip": ""
        },
        "calm": {
            "songs": [
                "https://youtu.be/Doo1T5WabEU?si=dBnmr5iD1Nw3-dTC",  
                "https://youtu.be/wLBrjrcMlCo?si=Q5kCicDQoLbmn8RP", 
                "https://youtu.be/MDwgUE-TBVY?si=yJTty8-jbBn5bKz1",  
                "https://youtu.be/2DNtm_KNVNQ?si=FSoVFdTzHwbHg6CI"  
            ],
            "tip": ""
        }
    },
    
    "haryanvi": {
    "happy": {
        "songs": [
            "https://youtu.be/OulN7vTDq1I?si=_y8oT0xHtfDJMD2p",  
            "https://youtu.be/vbaww9S3i8o?si=9qQu-0KD4NCZ7Tqp", 
            "https://youtu.be/cXpkvG4MuW4?si=0UfEmOflyEEwaBZs",  
            "https://youtu.be/PRiSzXKA2OY?si=mH6C2TyzAD-WYdD9"   
        ],
        "tip": ""
    },
    "sad": {
        "songs": [
            "https://youtu.be/o1tWazvhObc?si=YpH1IXPD4pHt5Ta1",  
            "https://youtu.be/NrN66D-Dj2o?si=VCT72dno5mv-Oq9r",  
            "https://youtu.be/J0rEeO3HFv8?si=wz6YZkGvquDgWMwA",  
            "https://youtu.be/nM-OKWu5OXk?si=RnJodqBT8uJVAGwE"  
        ],
        "tip": ""
    },
    "romantic": {
        "songs": [
            "https://youtu.be/T-ONOkhGITE?si=dkPE4AdkpUFmdVX2",  
            "https://youtu.be/cehyr946p64?si=TRUFLs5icAAmPoVc",  
            "https://youtu.be/AMQIiEea12A?si=Z7gYRKaoXkju30gr", 
            "https://youtu.be/tnlnqTRV5ZQ?si=CdX3qrENOHnL60W2"   
        ],
        "tip": ""
    },
    "energetic": {
        "songs": [
            "https://youtu.be/obgMGM6I2rE?si=F8twDCkHwUAlxCsq",  
            "https://youtu.be/szUSkYTXq7A?si=e2pvqXSU6vo7dRnZ",  
            "https://youtu.be/ZeaqjybbzzM?si=_3PsDYTdR_9PaQGa",
            "https://youtu.be/QJdw4OUWyRY?si=8KAh5nECQ6q9TVZE", 
            "https://youtu.be/3oOGF8P1BJo?si=IDm7mpEH7NjUBPZL"   
        ],
        "tip": ""
    },
    "calm": {
        "songs": [
            "https://youtu.be/NGPMKB93urc?si=m6sGu6Juf7Ydzcpy", 
            "https://youtu.be/Y17jJEj49AM?si=78yLg69HPXmJmgcM",  
            "https://youtu.be/OYf9NlA8AeU?si=5m17c5Sdmspe0y6W", 
            "https://youtu.be/DTJQzZpQtps?si=bxj00d39TX6xeSY2"  
        ],
        "tip": ""
    }
},


    "bhojpuri": {
        "happy": {
            "songs": [
                "https://youtu.be/4GRpdIV5DAQ?si=uwV-OlotfuB_ZD0_", 
                "https://youtu.be/zmwfd8x0DrM?si=RUb3YqsNY4UfEZsC",  
                "https://youtu.be/xyF0AR1r8OQ?si=sK2EXB5FnZnPrzeR",  
                "https://youtu.be/fDS-a4JDRpk?si=1vf3pGOU7TNiyQ85"   
            ],
            "tip": ""
        },
        "sad": {
            "songs": [
                "https://youtu.be/RL66qL8w_PI?si=bNDUkrqY3r-L0uY_", 
                "https://youtu.be/mcGyZSkIHKs?si=yvdtnn53L6yTx0iT",  
                "https://youtu.be/SJ9T6nRpDCM?si=jSGXeOsvRFO_3Uip", 
                "https://youtu.be/-uwbenvdiFk?si=meQXm2czmHitFGj6"   
            ],
            "tip": ""
        },
        "romantic": {
            "songs": [
                "https://youtu.be/sAloiE9-OIA?si=QcCDsUejfjO2iHk9",  
                "https://youtu.be/j1PFv7qIPXo?si=TOaTit500sw1VWhL", 
                "https://youtu.be/VfTUwCyNmzw?si=qoY_QUj_qZqxuKTG",  
                "https://youtu.be/9K37GCNyQgY?si=Pfs1B956zdrqHvQM"   
            ],
            "tip": ""
        },
        "energetic": {
            "songs": [
                "https://youtu.be/DYO_GLIWlRA?si=mIHdyxfvl1SJUKDd",  
                "https://youtu.be/0c7vj-y5QCs?si=znQesBaWSD7INnPA", 
                "https://youtu.be/SIsGR0-SQf0?si=4LLvi0-7Exjrbnfd",  
                "https://youtu.be/__bM37E9vws?si=WOVkrr6hgJvfdIZu"   
            ],
            "tip": ""
        },
        "calm": {
            "songs": [
                "https://youtu.be/TyfYty3WCb4?si=cKGnoNBSQpmbCgn5", 
                "https://youtu.be/MXeRQg9CmSM?si=ZgOuKHk-GM1Fpvl0",  
                "https://youtu.be/Gk60zlZvZuA?si=kgfMcquzuri2iblk",  
                "https://youtu.be/mRUz_E3JzWQ?si=qtBLM8UNu5oEXaIm"  
            ],
            "tip": ""
        }
    },

    "english": {
        "happy": {
            "songs": [
                "https://youtu.be/ru0K8uYEZWw?si=4i6ZyTJr335DyfEf",  
                "https://youtu.be/ZbZSe6N_BXs?si=3SKKiA8DplqUo025",  
                "https://youtu.be/fLexgOxsZu0?si=MCcXbcwmCXi60gMJ", 
                "https://youtu.be/zg49cOyfREc?si=R6H2mrlezvCt6-5W"   
            ],
            "tip": ""
        },
        "sad": {
            "songs": [
                "https://youtu.be/jLNrvmXboj8?si=nStvsymYYmM99JLF",  
                "https://youtu.be/V1Pl8CzNzCw?si=d08Hj3p9HxWrwfxI", 
                "https://youtu.be/ALM--Jeb-6c?si=tD74IRRUe0wSNmOM", 
                "https://youtu.be/zgaCZOQCpp8?si=1iVtkseOtNAtmOEv"   
            ],
            "tip": ""
        },
        "romantic": {
            "songs": [
                "https://youtu.be/AJtDXIazrMo?si=IGU6ahPeO3kfJHbe", 
                "https://youtu.be/lp-EO5I60KA?si=7q8kbmnQbXSG49VJ",  
                "https://youtu.be/lWA2pjMjpBs?si=Uo1WNCcqdCzloBnI",  
                "https://youtu.be/bo_efYhYU2A?si=mj8DP5qk5XOzvxXt"   
            ],
            "tip": ""
        },
        "energetic": {
            "songs": [
                "https://youtu.be/hHB1Ikzfpmc?si=dCqLyNOJQP74PAgV", 
                "https://youtu.be/d6_9CF1ucoI?si=QOVWn0ttIo5k-8Kj", 
                "https://youtu.be/Yn6w6sbyzug?si=B0gEiuP-u7qGYfLG",  
                "https://youtu.be/whwe0KD_rGw?si=nzSmsjcgdrQhkXy1"   
            ],
            "tip": ""
        },
        "calm": {
            "songs": [
                "https://youtu.be/4adZ7AguVcw?si=NFLaQoUW0oS7BBuO", 
                "https://youtu.be/jLNrvmXboj8?si=vagDgRoiRfoGSBn3",  
                "https://youtu.be/mk3XycambgI?si=mDwATxS5IxxpJv57",  
                "https://youtu.be/V9PVRfjEBTI?si=nAcaSuGIUYmAV3Iz"   
            ],
            "tip": ""
        }
    }
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get('mood')
    language = request.form.get('language', 'hindi') 

    if language in mood_data and mood in mood_data[language]:
        import requests
        import re
        song = random.choice(mood_data[language][mood]["songs"])
        # Extract video ID from URL
        match = re.search(r"(?:v=|be/)([\w-]+)", song)
        video_id = match.group(1) if match else None
        # Embed YouTube API key
        import os
        YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
        song_title = "Unknown Song"
        if video_id:
            api_url = f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={YOUTUBE_API_KEY}&part=snippet"
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    data = response.json()
                    items = data.get("items")
                    if items and len(items) > 0:
                        song_title = items[0]["snippet"]["title"]
            except Exception:
                pass
        return render_template('index.html', song=song, song_title=song_title, mood=mood)
    else:
        return render_template('index.html', error="Invalid mood or language selected.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
