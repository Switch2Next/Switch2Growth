from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index-3.html") #inside templates/



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)

