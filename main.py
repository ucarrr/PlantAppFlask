from flask import  Flask,request,render_template,redirect,url_for


app=Flask(__name__)

@app.route("/")
def index():
      return render_template("/index.html", number = 10 )
  
  
@app.route("/delete/item")
def delete():
      return ('Delete Item')
  

@app.route("/delete/<string:id>")
def deleteId(id):
      return ("Id : "+ id)
  

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid... Please try again.'
            print("invalid");
        else:
            username=request.form.get('username')
            password=request.form.get('password')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)
   




if __name__== "__main__":
    app.run(debug=True)
   