from flask import Flask
from threading import Thread

# Inisialisasi aplikasi Flask
app = Flask('')

# Endpoint utama untuk memastikan bot berjalan
@app.route('/')
def home():
    return "Bot is running!"


# Fungsi untuk menjalankan server Flask
def run():
    try:
        app.run(host='0.0.0.0', port=5000)
    except Exception as e:
        print(f"Error: {e}")


# Fungsi untuk menjaga server tetap hidup di thread terpisah
def keep_alive():
    t = Thread(target=run)
    t.start()
