from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/Gas")
def Gas():
   return render_template("Gas.html")

@app.route("/Liquid")
def Liquid():
   return render_template("Liquid.html")

@app.route("/Solid")
def Solid():
   return render_template("Solid.html")

   
@app.route("/Plasma")
def Plasma():
   return render_template("Plasma.html")

@app.route("/success/<name>")
def success(name):
    return "Welcome %s" % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == "__main__":
   app.run()