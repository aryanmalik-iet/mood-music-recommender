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
                "https://youtu.be/41iEgelUUzM?si=cY0JBUQXarjBHIe_"   # 
            ],
            "tip": "Zindagi ka maza lo, smile karke nach lo! 😄"
        },
        "sad": {
            "songs": [
                "https://youtu.be/lBvbNxiVmZA?si=hqMnGCKsJZJWVgkE",  
                "https://youtu.be/sVRwZEkXepg?si=D7ZigJ442gShacvW", 
                "https://youtu.be/1poXN3jF3Bw?si=HcoB6e8eKHt7JUN-", 
                "https://youtu.be/p9nYTT8KGeM?si=RQiRNgTLeY_Vfkqq"   
            ],
            "tip": "Toote dil ka ilaaj hota hai – ek acha gaana aur thoda waqt 💔"
        },
        "romantic": {
            "songs": [
                "https://youtu.be/RazuWp5kSHk?si=5vxafKPvFUI_DeOT",  
                "https://youtu.be/-8C_2BBVWk8?si=U3um0fPUOF78H7IB", 
                "https://youtu.be/gvyUuxdRdR4?si=UBM2vRzi-JtxXsep",  
                "https://youtu.be/gvyUuxdRdR4?si=UBM2vRzi-JtxXsep"   
            ],
            "tip": "Kisi ko yaad karo, dil se. Shayad uska msg aa jaye 💌"
        },
        "energetic": {
            "songs": [
                "https://youtu.be/HoCwa6gnmM0?si=2K7oXNmNlXn3jQ71", 
                "https://youtu.be/abiL84EAWSY?si=D1IVnvi-zpOyNsN9",  
                "https://youtu.be/puKD3nkB1h4?si=eJAk4bv7VqUR0BPL",  
                "https://youtu.be/IjBAgWKW12Y?si=4od6_AScIcP3_Obu"   
            ],
            "tip": "Yeh energy kahin chhupa ke na rakho — duniya hila do ⚡"
        },
        "calm": {
            "songs": [
                "https://youtu.be/fSS_R91Nimw?si=YwdT03Y5DZqGhAVK", 
                "https://youtu.be/uVTdmJIcjtQ?si=72iCHVuJoMMj-PRD",  
                "https://youtu.be/JHUrRSBtUNE?si=bfSshxrOaaadVETM",  
                "https://youtu.be/sK7riqg2mr4?si=VjBxK1x6MDQ-dLmn"   
            ],
            "tip": "Shaanti mein hi shakti hai. Saans le aur feel kar 🧘‍♂️"
        }
    },

    "punjabi": {
        "happy": {
            "songs": [
                "https://youtu.be/PjTU0DmBWiU?si=mW6Ubli4VAZEUclO",  # Lehanga
                "https://youtu.be/Q-GOFPM01d0?si=BaFkEevY58_LaaNe",  # 3 Peg
                "https://youtu.be/n3mJ9b6l33E?si=eyMveD-UrTrUvTNK",  # So High
                "https://youtu.be/qgbvMJsz1Rk?si=_v4RevjIZTFz8yfz"   # Naah
            ],
            "tip": "Balle balle! Punjabiyan di vibe kuch aur hi hai 🕺"
        },
        "sad": {
            "songs": [
                "https://youtu.be/jynMDYYFB9I?si=4UoEoBQUQ337kHjC",  # Sidhu Moose Wala - The Last Ride
                "https://youtu.be/QHJstKwI0Ic?si=0laHUPNjE3aR1ppX",  # Jatt Di Pasand
                "https://youtu.be/enQuoRciccM?si=ZipmWT7XrNA_kHvc",  # Baarish Ki Jaaye
                "https://youtu.be/Wd6TufgP3qs?si=zZ4u917V3_sGfMNs"   # Paigam
            ],
            "tip": "Thoda dard bhi zaroori hai... jiven geet vich 💔"
        },
        "romantic": {
            "songs": [
                "https://youtu.be/X1xub3f7ubY?si=SvLrfJqwATz22kDF",  
                "https://youtu.be/_RywJ_FJ_3U?si=oQ7NI3l8dBZnOC8b",  
                "https://youtu.be/9udS0mpi1L4?si=yRlYZShcD85gKF6Q",  
                "https://youtu.be/jn77BhLMGc8?si=WXbGCRD0bOVyvFMh"   
            ],
            "tip": "Punjabi romance = swag + feeling 💘"
        },
        "energetic": {
            "songs": [
                "https://youtu.be/RLhuPD2ASKE?si=v7DgBlFwqa6a5IYM",  
                "https://youtu.be/tpFljbJxZiw?si=eIGBvGcXCiLZ5sJT", 
                "https://youtu.be/GgmFC8y8q3k?si=4CBeKQRRQ74hGDqv",  
                "https://youtu.be/6xoB4ZiKKn0?si=gcMhr1bVOStz7_SJ"   
            ],
            "tip": "Gabru da swag! Energy full on 🔥"
        },
        "calm": {
            "songs": [
                "https://youtu.be/Doo1T5WabEU?si=dBnmr5iD1Nw3-dTC",  # Baarish
                "https://youtu.be/wLBrjrcMlCo?si=Q5kCicDQoLbmn8RP",  # Sakhiyaan
                "https://youtu.be/MDwgUE-TBVY?si=yJTty8-jbBn5bKz1",  # Rataan
                "https://youtu.be/2DNtm_KNVNQ?si=FSoVFdTzHwbHg6CI"   # Khaab
            ],
            "tip": "Dheere bol, halke sun. Sohne geet, sukoon wali feeling 🧘"
        }
    },
    
    "haryanvi": {
    "happy": {
        "songs": [
            "https://youtu.be/OulN7vTDq1I?si=_y8oT0xHtfDJMD2p",  # DJ Waley Babu - Badshah
            "https://youtu.be/vbaww9S3i8o?si=9qQu-0KD4NCZ7Tqp",  # Haryanvi Mashup
            "https://youtu.be/cXpkvG4MuW4?si=0UfEmOflyEEwaBZs",  # Gajender Phogat - Solid Body
            "https://youtu.be/PRiSzXKA2OY?si=mH6C2TyzAD-WYdD9"   # DJ Wale Babu Remix
        ],
        "tip": "Khush raho, naacho, gaao, zindagi ka maza lo! 😄"
    },
    "sad": {
        "songs": [
            "https://youtu.be/o1tWazvhObc?si=YpH1IXPD4pHt5Ta1",  # Teri Aakhya Ka Yo Kajal - Sapna Choudhary
            "https://youtu.be/NrN66D-Dj2o?si=VCT72dno5mv-Oq9r",  # Chhoti Chhoti Baatein
            "https://youtu.be/J0rEeO3HFv8?si=wz6YZkGvquDgWMwA",  # Dushmani
            "https://youtu.be/nM-OKWu5OXk?si=RnJodqBT8uJVAGwE"   # Meri Baat Sun Le O Saathi
        ],
        "tip": "Dard ko mehsoos karo, par aage badho. Zindagi chalti rahegi 💙"
    },
    "romantic": {
        "songs": [
            "https://youtu.be/T-ONOkhGITE?si=dkPE4AdkpUFmdVX2",  # Haryanvi Romantic Song - Raju Punjabi
            "https://youtu.be/cehyr946p64?si=TRUFLs5icAAmPoVc",  # Tera Yaar Hoon Main (Haryanvi Cover)
            "https://youtu.be/AMQIiEea12A?si=Z7gYRKaoXkju30gr",  # Pyaar Karunga
            "https://youtu.be/tnlnqTRV5ZQ?si=CdX3qrENOHnL60W2"   # Tere Bin
        ],
        "tip": "Dil se pyaar karo, bina dare 💘"
    },
    "energetic": {
        "songs": [
            "https://youtu.be/obgMGM6I2rE?si=F8twDCkHwUAlxCsq",  
            "https://youtu.be/szUSkYTXq7A?si=e2pvqXSU6vo7dRnZ",  
            "https://youtu.be/ZeaqjybbzzM?si=_3PsDYTdR_9PaQGa",
            "https://youtu.be/QJdw4OUWyRY?si=8KAh5nECQ6q9TVZE", 
            "https://youtu.be/3oOGF8P1BJo?si=IDm7mpEH7NjUBPZL"   
        ],
        "tip": "Energy ko channelize karo, aaj kuch bada karo! 🔥"
    },
    "calm": {
        "songs": [
            "https://youtu.be/NGPMKB93urc?si=m6sGu6Juf7Ydzcpy",  # Haryanvi Soft Song
            "https://youtu.be/Y17jJEj49AM?si=78yLg69HPXmJmgcM",  # Soothing Haryanvi Melody
            "https://youtu.be/OYf9NlA8AeU?si=5m17c5Sdmspe0y6W",  # Calm Vibes - Haryanvi
            "https://youtu.be/DTJQzZpQtps?si=bxj00d39TX6xeSY2"   # Relaxing Haryanvi Tune
        ],
        "tip": "Shaanti se baitho, dhyaan do apne dil ko 🧘‍♂️"
    }
},


    "bhojpuri": {
        "happy": {
            "songs": [
                "https://youtu.be/4GRpdIV5DAQ?si=uwV-OlotfuB_ZD0_",  # Lollipop Lagelu
                "https://youtu.be/zmwfd8x0DrM?si=RUb3YqsNY4UfEZsC",  # Chhalakata Hamro Jawaniya
                "https://youtu.be/xyF0AR1r8OQ?si=sK2EXB5FnZnPrzeR",  # Lagdi Lahore Di
                "https://youtu.be/fDS-a4JDRpk?si=1vf3pGOU7TNiyQ85"   # Raja Tani Jai Na
            ],
            "tip": "Masti mein raho, nacho aur gaao! 🎉"
        },
        "sad": {
            "songs": [
                "https://youtu.be/RL66qL8w_PI?si=bNDUkrqY3r-L0uY_",  # Saiyan Ji Dilwa Mangelein
                "https://youtu.be/mcGyZSkIHKs?si=yvdtnn53L6yTx0iT",  # Phoolwa Ke Patunwa
                "https://youtu.be/SJ9T6nRpDCM?si=jSGXeOsvRFO_3Uip",  # Nimiya Ke Daar Maiya
                "https://youtu.be/-uwbenvdiFk?si=meQXm2czmHitFGj6"   # Humka Peeni Hai
            ],
            "tip": "Kabhi kabhi dard bhi gaane ko aur bhi gehra banata hai 💔"
        },
        "romantic": {
            "songs": [
                "https://youtu.be/sAloiE9-OIA?si=QcCDsUejfjO2iHk9",  # Tu Lagawelu Jab Lipistic
                "https://youtu.be/j1PFv7qIPXo?si=TOaTit500sw1VWhL",  # Patna Se Pakistan
                "https://youtu.be/VfTUwCyNmzw?si=qoY_QUj_qZqxuKTG",  # Bhatar Katani
                "https://youtu.be/9K37GCNyQgY?si=Pfs1B956zdrqHvQM"   # Raja Tani Jai Na
            ],
            "tip": "Dil se pyaar karo, gaane ke sath! 💕"
        },
        "energetic": {
            "songs": [
                "https://youtu.be/DYO_GLIWlRA?si=mIHdyxfvl1SJUKDd",  # Chhalakata Hamro Jawaniya
                "https://youtu.be/0c7vj-y5QCs?si=znQesBaWSD7INnPA",  # Bhatar Aiehe Holi Ke Baad
                "https://youtu.be/SIsGR0-SQf0?si=4LLvi0-7Exjrbnfd",  # Aara Hile Chapra Hile
                "https://youtu.be/__bM37E9vws?si=WOVkrr6hgJvfdIZu"   # Saiyan Ji Dilwa Mangelein
            ],
            "tip": "Energy ko release karo, full power se! 🔥"
        },
        "calm": {
            "songs": [
                "https://youtu.be/TyfYty3WCb4?si=cKGnoNBSQpmbCgn5",  # Pyar Ka Sahara
                "https://youtu.be/MXeRQg9CmSM?si=ZgOuKHk-GM1Fpvl0",  # Kahiya Se Aailu
                "https://youtu.be/Gk60zlZvZuA?si=kgfMcquzuri2iblk",  # Mehndi Laga Ke Rakhna
                "https://youtu.be/mRUz_E3JzWQ?si=qtBLM8UNu5oEXaIm"   # Saiyan Ji Dilwa Mangelein (Slow)
            ],
            "tip": "Dheere dheere sukoon bhari dhun me doob jao 🧘‍♂️"
        }
    },

    "english": {
        "happy": {
            "songs": [
                "https://youtu.be/ru0K8uYEZWw?si=4i6ZyTJr335DyfEf",  # Can't Stop the Feeling - JT
                "https://youtu.be/ZbZSe6N_BXs?si=3SKKiA8DplqUo025",  # Despacito (English version)
                "https://youtu.be/fLexgOxsZu0?si=MCcXbcwmCXi60gMJ",  # Get Lucky - Daft Punk
                "https://youtu.be/zg49cOyfREc?si=R6H2mrlezvCt6-5W"   # Wake Me Up - Avicii
            ],
            "tip": "Keep smiling and dance like no one's watching! 😄"
        },
        "sad": {
            "songs": [
                "https://youtu.be/jLNrvmXboj8?si=nStvsymYYmM99JLF",  # Someone Like You - Adele
                "https://youtu.be/V1Pl8CzNzCw?si=d08Hj3p9HxWrwfxI",  # Fix You - Coldplay
                "https://youtu.be/ALM--Jeb-6c?si=tD74IRRUe0wSNmOM",  # Hello - Adele
                "https://youtu.be/zgaCZOQCpp8?si=1iVtkseOtNAtmOEv"   # Skinny Love - Birdy
            ],
            "tip": "It's okay to feel down sometimes. Take your time 💙"
        },
        "romantic": {
            "songs": [
                "https://youtu.be/AJtDXIazrMo?si=IGU6ahPeO3kfJHbe",  # Perfect - Ed Sheeran
                "https://youtu.be/lp-EO5I60KA?si=7q8kbmnQbXSG49VJ",  # All of Me - John Legend
                "https://youtu.be/lWA2pjMjpBs?si=Uo1WNCcqdCzloBnI",  # I Won't Give Up - Jason Mraz
                "https://youtu.be/bo_efYhYU2A?si=mj8DP5qk5XOzvxXt"   # Thinking Out Loud - Ed Sheeran
            ],
            "tip": "Love is in the air! Send someone a sweet message 💌"
        },
        "energetic": {
            "songs": [
                "https://youtu.be/hHB1Ikzfpmc?si=dCqLyNOJQP74PAgV",  # Eye of the Tiger - Survivor
                "https://youtu.be/d6_9CF1ucoI?si=QOVWn0ttIo5k-8Kj",  # Uptown Funk - Bruno Mars
                "https://youtu.be/Yn6w6sbyzug?si=B0gEiuP-u7qGYfLG",  # Can't Hold Us - Macklemore
                "https://youtu.be/whwe0KD_rGw?si=nzSmsjcgdrQhkXy1"   # Happy - Pharrell Williams
            ],
            "tip": "Use this energy to conquer your day! 💥"
        },
        "calm": {
            "songs": [
                "https://youtu.be/4adZ7AguVcw?si=NFLaQoUW0oS7BBuO",  # River Flows in You - Yiruma
                "https://youtu.be/jLNrvmXboj8?si=vagDgRoiRfoGSBn3",  # Weightless - Marconi Union
                "https://youtu.be/mk3XycambgI?si=mDwATxS5IxxpJv57",  # Clair de Lune - Debussy
                "https://youtu.be/V9PVRfjEBTI?si=nAcaSuGIUYmAV3Iz"   # Spiegel im Spiegel - Arvo Pärt
            ],
            "tip": "Stay calm and let the music heal your soul 🧘‍♂️"
        }
    }
}



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form.get('mood')
    language = request.form.get('language', 'hindi')  # Default to Hindi if nothing selected

    if language in mood_data and mood in mood_data[language]:
        song = random.choice(mood_data[language][mood]["songs"])
        tip = mood_data[language][mood]["tip"]
        return render_template('index.html', song=song, tip=tip, mood=mood)
    else:
        return render_template('index.html', error="Invalid mood or language selected.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
