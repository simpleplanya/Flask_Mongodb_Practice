from flask import Flask
app = Flask(__name__)

#In fact it (app.route) call add_url_rule() function 
@app.route("/")
def hello():
    return "hello World"


if __name__ == "__main__":
    app.run()
