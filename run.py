from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/s")
def services():
    return render_template("services.html")

@app.route("/e")
def events():
    return render_template("events.html")
    
@app.route("/c")
def contact():
    return render_template("contact.html")

@app.route("/p")
def payment():
    return render_template("payment.html")

@app.route("/f")
def faq():
    return render_template("faq.html")

    
if __name__ == "__main__":
    app.run(debug=True)