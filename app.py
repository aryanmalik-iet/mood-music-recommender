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
            "https://youtu.be/ZZ86YrRjIOs?si=-BpqgvwyBpv8-MVn"   
        ],
        "tip": "Energy ko channelize karo, aaj kuch bada karo! 🔥"
    },
    "calm": {
        "songs": [
            "https://youtu.be/NGPMKB93urc?si=m6sGu6Juf7Ydzcpy",  # Haryanvi Soft Song
            "https://youtu.be/Y17jJEj49AM?si=78yLg69HPXmJmgcM",  # Soothing Haryanvi Melody
            "https://www.youtube.com/watch?v=t17aQTCYrTU",  # Calm Vibes - Haryanvi
            "https://www.youtube.com/watch?v=kUiXktZnmQc"   # Relaxing Haryanvi Tune
        ],
        "tip": "Shaanti se baitho, dhyaan do apne dil ko 🧘‍♂️"
    }
},


    "bhojpuri": {
        "happy": {
            "songs": [
                "https://www.youtube.com/watch?v=fmF2my-WVd0",  # Lollipop Lagelu
                "https://www.youtube.com/watch?v=6i6pM1Yhvjc",  # Chhalakata Hamro Jawaniya
                "https://www.youtube.com/watch?v=3lX5Euf01xA",  # Lagdi Lahore Di
                "https://www.youtube.com/watch?v=K1IepWHmEGo"   # Raja Tani Jai Na
            ],
            "tip": "Masti mein raho, nacho aur gaao! 🎉"
        },
        "sad": {
            "songs": [
                "https://www.youtube.com/watch?v=mEOkmk1G8o8",  # Saiyan Ji Dilwa Mangelein
                "https://www.youtube.com/watch?v=KDyfNcJc0IE",  # Phoolwa Ke Patunwa
                "https://www.youtube.com/watch?v=7qhuL3-KnXg",  # Nimiya Ke Daar Maiya
                "https://www.youtube.com/watch?v=w3l9xgUPHeM"   # Humka Peeni Hai
            ],
            "tip": "Kabhi kabhi dard bhi gaane ko aur bhi gehra banata hai 💔"
        },
        "romantic": {
            "songs": [
                "https://www.youtube.com/watch?v=nClKShDb4Ts",  # Tu Lagawelu Jab Lipistic
                "https://www.youtube.com/watch?v=VQZDLpzMYHs",  # Patna Se Pakistan
                "https://www.youtube.com/watch?v=DC6U2vVK5xc",  # Bhatar Katani
                "https://www.youtube.com/watch?v=Oq9Lq7yK2lc"   # Raja Tani Jai Na
            ],
            "tip": "Dil se pyaar karo, gaane ke sath! 💕"
        },
        "energetic": {
            "songs": [
                "https://www.youtube.com/watch?v=FzqP-HVKpAI",  # Chhalakata Hamro Jawaniya
                "https://www.youtube.com/watch?v=GCplE_PfC8k",  # Bhatar Aiehe Holi Ke Baad
                "https://www.youtube.com/watch?v=7vg8mxPZj18",  # Aara Hile Chapra Hile
                "https://www.youtube.com/watch?v=HLG09mK2TgQ"   # Saiyan Ji Dilwa Mangelein
            ],
            "tip": "Energy ko release karo, full power se! 🔥"
        },
        "calm": {
            "songs": [
                "https://www.youtube.com/watch?v=LsA6JsRYgnE",  # Pyar Ka Sahara
                "https://www.youtube.com/watch?v=XZPcZRhVraM",  # Kahiya Se Aailu
                "https://www.youtube.com/watch?v=w8VrITmKUuQ",  # Mehndi Laga Ke Rakhna
                "https://www.youtube.com/watch?v=vSNW0XzryCg"   # Saiyan Ji Dilwa Mangelein (Slow)
            ],
            "tip": "Dheere dheere sukoon bhari dhun me doob jao 🧘‍♂️"
        }
    },

    "english": {
        "happy": {
            "songs": [
                "https://www.youtube.com/watch?v=3tmd-ClpJxA",  # Can't Stop the Feeling - JT
                "https://www.youtube.com/watch?v=kJQP7kiw5Fk",  # Despacito (English version)
                "https://www.youtube.com/watch?v=5NV6Rdv1a3I",  # Get Lucky - Daft Punk
                "https://www.youtube.com/watch?v=60ItHLz5WEA"   # Wake Me Up - Avicii
            ],
            "tip": "Keep smiling and dance like no one's watching! 😄"
        },
        "sad": {
            "songs": [
                "https://www.youtube.com/watch?v=hLQl3WQQoQ0",  # Someone Like You - Adele
                "https://www.youtube.com/watch?v=RB-RcX5DS5A",  # Fix You - Coldplay
                "https://www.youtube.com/watch?v=YQHsXMglC9A",  # Hello - Adele
                "https://www.youtube.com/watch?v=LG_WkDwA47c"   # Skinny Love - Birdy
            ],
            "tip": "It's okay to feel down sometimes. Take your time 💙"
        },
        "romantic": {
            "songs": [
                "https://www.youtube.com/watch?v=450p7goxZqg",  # Perfect - Ed Sheeran
                "https://www.youtube.com/watch?v=08Hr6gZJaeY",  # All of Me - John Legend
                "https://www.youtube.com/watch?v=Z0GFRcFm-aY",  # I Won't Give Up - Jason Mraz
                "https://www.youtube.com/watch?v=FlsBObg-1BQ"   # Thinking Out Loud - Ed Sheeran
            ],
            "tip": "Love is in the air! Send someone a sweet message 💌"
        },
        "energetic": {
            "songs": [
                "https://www.youtube.com/watch?v=1zjM7_qzLqk",  # Eye of the Tiger - Survivor
                "https://www.youtube.com/watch?v=btPJPFnesV4",  # Uptown Funk - Bruno Mars
                "https://www.youtube.com/watch?v=7wtfhZwyrcc",  # Can't Hold Us - Macklemore
                "https://www.youtube.com/watch?v=OPf0YbXqDm0"   # Happy - Pharrell Williams
            ],
            "tip": "Use this energy to conquer your day! 💥"
        },
        "calm": {
            "songs": [
                "https://www.youtube.com/watch?v=2OYq8TDXO9c",  # River Flows in You - Yiruma
                "https://www.youtube.com/watch?v=V2t7CwAyOyE",  # Weightless - Marconi Union
                "https://www.youtube.com/watch?v=K1vjb3nS9Y0",  # Clair de Lune - Debussy
                "https://www.youtube.com/watch?v=9auOCbH5Ns4"   # Spiegel im Spiegel - Arvo Pärt
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
