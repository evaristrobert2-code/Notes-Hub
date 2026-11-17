from flask import Flask, render_template
app = Flask(__name__)
notes=[
    {"title":"COMPUTER FUNDAMENTALS AND APPLICATIONS","course":"IS052"},
    {"title":"COMPUTER ARCHITECTURE AND ORGANISATION","course":'IS064'},
    {'title':"INFORMATION SYSTEMS AND ETHICS","course":'IS063'}
]
@app.route("/")
def home():
    return render_template("index.html",notes=notes)
if __name__ == '__main__':
    app.run(debug=True)