from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! how are you?????"
# run the app.
if __name__ == "__main__":
    app.run()
