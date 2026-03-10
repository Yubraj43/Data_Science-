from flask import Flask, render_template, request 
app = Flask(__name__, template_folder="templates")  # Specify the templates folder
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/index")
def index():
    return render_template("index.html", methods=["GET",])

@app.route("/form",  methods=["GET", "POST"])
def form():
      if request.method == "POST":
        # Process form data
        name = request.form["name"]
        email = request.form["email"]
        return f"your {name} and {email} have been received!"
       
      return render_template("form.html")
    

@app.route("/submit",  methods=[" GET","POST"])
def submit_form():
      if request.method == "POST":
        # Process form data
        name = request.form["name"]
        email = request.form["email"]
        return f" {name}  your information has been received!"
       
      return render_template("form.html")   
   
        # Do something with the form data (e.g., save to database, send email, etc.)
        #  return render_template("form.html", methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
