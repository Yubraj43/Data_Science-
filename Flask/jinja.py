from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, Flask!" 
@app.route("/success/<int:score>")
def success(score):
  result = ""
  if score >= 50:
    result = "You passed!"
  else:    result = "You failed!"
  return render_template("result.html", result=result)



if __name__ == "__main__":
    app.run(debug=True)