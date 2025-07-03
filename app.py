from flask import Flask, render_template, request
import random

app = Flask(__name__)

mood_data = {
    "hindi": {
        "happy": {
            "songs": [
                "https://www.youtube.com/watch?v=BddP6PYo2gs",  # Dance Ka Bhoot
                "https://www.youtube.com/watch?v=jFxQ8zG4Lz0",  # Guli Mata
                "https://www.youtube.com/watch?v=6xKWiCMKKJg",  # Nadiyon Paar
                "https://www.youtube.com/watch?v=rnqL8qT3v8I"   # Kala Chashma
            ],
            "tip": "Zindagi ka maza lo, smile karke nach lo! 😄"
        },
        "sad": {
            "songs": [
                "https://www.youtube.com/watch?v=VZvzvLiGUtw",  # Mann Bharryaa
                "https://www.youtube.com/watch?v=4DTljc5Cj00",  # Roke Na Ruke
                "https://www.youtube.com/watch?v=7vh2Y2cL4pQ",  # Tujhe Bhula Diya
                "https://www.youtube.com/watch?v=eW3tQbiD6sE"   # Channa Mereya
            ],
            "tip": "Toote dil ka ilaaj hota hai – ek acha gaana aur thoda waqt 💔"
        },
        "romantic": {
            "songs": [
                "https://www.youtube.com/watch?v=3j8ecF8Wt4E",  # Raataan Lambiyan
                "https://www.youtube.com/watch?v=5bYMAgM42pM",  # Maan Meri Jaan
                "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Love Me Like You Do
                "https://www.youtube.com/watch?v=SH8kqnGPPac"   # Tum Se Hi
            ],
            "tip": "Kisi ko yaad karo, dil se. Shayad uska msg aa jaye 💌"
        },
        "energetic": {
            "songs": [
                "https://www.youtube.com/watch?v=fLexgOxsZu0",  # Uptown Funk (Hindi audience fav)
                "https://www.youtube.com/watch?v=Bh0b2kPo98Q",  # Apna Time Aayega
                "https://www.youtube.com/watch?v=K0ibBPhiaG0",  # Malhari
                "https://www.youtube.com/watch?v=VgQUdD9zXKw"   # Zinda - Bhaag Milkha Bhaag
            ],
            "tip": "Yeh energy kahin chhupa ke na rakho — duniya hila do ⚡"
        },
        "calm": {
            "songs": [
                "https://www.youtube.com/watch?v=y3M6B5IuQ_4",  # Tum Mile Lo-Fi
                "https://www.youtube.com/watch?v=w_P-oN-nxdo",  # Lo Maan Liya
                "https://www.youtube.com/watch?v=QxrQ6BaijAY",  # Safarnama
                "https://www.youtube.com/watch?v=avz06PDqDbM"   # Dil Diyan Gallan Lo-Fi
            ],
            "tip": "Shaanti mein hi shakti hai. Saans le aur feel kar 🧘‍♂️"
        }
    },

    "punjabi": {
        "happy": {
            "songs": [
                "https://www.youtube.com/watch?v=xOeI4JcD2Jg",  # Lehanga
                "https://www.youtube.com/watch?v=7RdW56z4_yU",  # 3 Peg
                "https://www.youtube.com/watch?v=J3UjzRy7T_w",  # So High
                "https://www.youtube.com/watch?v=ACJQ2I3rEfw"   # Naah
            ],
            "tip": "Balle balle! Punjabiyan di vibe kuch aur hi hai 🕺"
        },
        "sad": {
            "songs": [
                "https://www.youtube.com/watch?v=1T5NuI6Ai-o",  # Sidhu Moose Wala - The Last Ride
                "https://www.youtube.com/watch?v=O3bAbKSFqJ8",  # Jatt Di Pasand
                "https://www.youtube.com/watch?v=7V_gj1tG8Dg",  # Baarish Ki Jaaye
                "https://www.youtube.com/watch?v=VQzW_bkOtQM"   # Paigam
            ],
            "tip": "Thoda dard bhi zaroori hai... jiven geet vich 💔"
        },
        "romantic": {
            "songs": [
                "https://www.youtube.com/watch?v=qKk6B3-59VE",  # Excuses – A.P. Dhillon
                "https://www.youtube.com/watch?v=jN__csTtRr4",  # Bijlee Bijlee
                "https://www.youtube.com/watch?v=3FikYj1hG1s",  # Brown Munde
                "https://www.youtube.com/watch?v=5N7_5kF_Pz8"   # Qismat
            ],
            "tip": "Punjabi romance = swag + feeling 💘"
        },
        "energetic": {
            "songs": [
                "https://www.youtube.com/watch?v=Z-FxR0xGs_k",  # GOAT – Sidhu Moosewala
                "https://www.youtube.com/watch?v=fkGfIR1y1K0",  # Same Beef
                "https://www.youtube.com/watch?v=sWzP2ZBV3Wg",  # Lamborghini
                "https://www.youtube.com/watch?v=-B2SnvQZZYw"   # Sher Aaya Sher
            ],
            "tip": "Gabru da swag! Energy full on 🔥"
        },
        "calm": {
            "songs": [
                "https://www.youtube.com/watch?v=snYhAXhCWWk",  # Baarish
                "https://www.youtube.com/watch?v=WU5N2ZjjGBk",  # Sakhiyaan
                "https://www.youtube.com/watch?v=2Z9_2-HNqWA",  # Rataan
                "https://www.youtube.com/watch?v=TeTrZP9P1fI"   # Khaab
            ],
            "tip": "Dheere bol, halke sun. Sohne geet, sukoon wali feeling 🧘"
        }
    },
    
    "haryanvi": {
    "happy": {
        "songs": [
            "https://www.youtube.com/watch?v=9ySPQynI6Ww",  # DJ Waley Babu - Badshah
            "https://www.youtube.com/watch?v=OxmIb4j8xvE",  # Haryanvi Mashup
            "https://www.youtube.com/watch?v=zWhXIxk8FEI",  # Gajender Phogat - Solid Body
            "https://www.youtube.com/watch?v=g0bzR3E1WJA"   # DJ Wale Babu Remix
        ],
        "tip": "Khush raho, naacho, gaao, zindagi ka maza lo! 😄"
    },
    "sad": {
        "songs": [
            "https://www.youtube.com/watch?v=03O9d1pFr8w",  # Teri Aakhya Ka Yo Kajal - Sapna Choudhary
            "https://www.youtube.com/watch?v=duUey2RxY2Y",  # Chhoti Chhoti Baatein
            "https://www.youtube.com/watch?v=JuLdWY9e1QE",  # Dushmani
            "https://www.youtube.com/watch?v=3J3FPl87-gk"   # Meri Baat Sun Le O Saathi
        ],
        "tip": "Dard ko mehsoos karo, par aage badho. Zindagi chalti rahegi 💙"
    },
    "romantic": {
        "songs": [
            "https://www.youtube.com/watch?v=lIGeTnFf90A",  # Haryanvi Romantic Song - Raju Punjabi
            "https://www.youtube.com/watch?v=9tx_M0U8pP4",  # Tera Yaar Hoon Main (Haryanvi Cover)
            "https://www.youtube.com/watch?v=FCZeh8nt5_Y",  # Pyaar Karunga
            "https://www.youtube.com/watch?v=RhV1hzPUEhM"   # Tere Bin
        ],
        "tip": "Dil se pyaar karo, bina dare 💘"
    },
    "energetic": {
        "songs": [
            "https://www.youtube.com/watch?v=GE6C1gNUhXA",  # Haryanvi Rap Song - MC Altaf
            "https://www.youtube.com/watch?v=_LKrr0zKa8k",  # Haryanvi DJ Remix
            "https://www.youtube.com/watch?v=dQw4w9WgXcQ",  # (Just an example, replace with real energetic song)
            "https://www.youtube.com/watch?v=OLxdhNKu1Cs"   # Desi Hip-Hop Haryanvi
        ],
        "tip": "Energy ko channelize karo, aaj kuch bada karo! 🔥"
    },
    "calm": {
        "songs": [
            "https://www.youtube.com/watch?v=txhSdTNsZXw",  # Haryanvi Soft Song
            "https://www.youtube.com/watch?v=VX4uUJxv7f4",  # Soothing Haryanvi Melody
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
