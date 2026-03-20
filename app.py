from flask import Flask, request, render_template

app = Flask(__name__)

def analyze(text):
    return {
        "summary": text[:100],
        "key_points": ["Point 1", "Point 2"],
        "questions": ["What is the main idea?"]
    }

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = analyze(text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
