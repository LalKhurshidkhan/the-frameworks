from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask World!"

if __name__ == '__main__':
    print("✅ Starting Flask app...")
    app.run(debug=True)
