from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
    <head><title>☁️ Azure App Service - Putri</title></head>
    <body style="font-family: Arial; text-align: center; margin-top: 10%; background: #f9f9f9;">
        <h1>✨ Halo, saya Putri Cellyenda!</h1>
        <p>🎓 Mahasiswa Informatika UAI</p>
        <p>🚀 Deployed to Azure App Service via GitHub</p>
        <p><small>Praktik Cloud Computing — Desember 2025</small></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
