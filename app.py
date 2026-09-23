from flask import Flask, render_template

app = Flask(__name__)

# Count how many common passwords are in our small list
def count_passwords():
    f = open("rules/common_passwords.txt")
    n = 0
    for line in f:
        if line.strip() != "":
            n = n + 1
    f.close()
    return n

@app.route("/")
def home():
    n = count_passwords()
    return render_template("index.html", common_count=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
