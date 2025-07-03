from flask import Flask, render_template, request
import random
import webbrowser

app = Flask(__name__)

mood_data = {
    "happy": {
        "songs": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=fLexgOxsZu0"
        ],
        "tip": "Stay present and enjoy the moment 🌞. Spread your smile!"
    },
    "sad": {
        "songs": [
            "https://www.youtube.com/watch?v=RgKAFK5djSk",
            "https://www.youtube.com/watch?v=J_ub7Etch2U"
        ],
        "tip": "It’s okay to feel low. Take a deep breath and allow yourself time to heal 💙."
    },
    "romantic": {
        "songs": [
            "https://www.youtube.com/watch?v=450p7goxZqg",
            "https://www.youtube.com/watch?v=JGwWNGJdvx8"
        ],
        "tip": "Love is the music of the soul. Maybe send a sweet text today 💌"
    },
    "energetic": {
        "songs": [
            "https://www.youtube.com/watch?v=btPJPFnesV4",
            "https://www.youtube.com/watch?v=2vjPBrBU-TM"
        ],
        "tip": "Use this energy to crush your goals today! 💥"
    },
    "calm": {
        "songs": [
            "https://www.youtube.com/watch?v=r6zIGXun57U",
            "https://www.youtube.com/watch?v=2OYq8TDXO9c"
        ],
        "tip": "Stay grounded. Peace is power. 🧘‍♂️"
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    mood = request.form['mood']
    if mood in mood_data:
        song = random.choice(mood_data[mood]["songs"])
        tip = mood_data[mood]["tip"]
        return render_template('index.html', song=song, tip=tip, mood=mood)
    else:
        return render_template('index.html', error="Invalid mood selected.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
