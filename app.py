from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Visual NetPol — CI/CD is alive. 🚀"

if __name__ == "__main__":
    # listen on all interfaces, port 8080 so docker can map it
    app.run(host="0.0.0.0", port=8080)
