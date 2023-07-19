from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/product')
def productpage():
    return render_template("product.html")

@app.route('/product2')
def productpage2():
    return render_template("product2.html")

@app.route('/product3')
def productpage3():
    return render_template("product3.html")

@app.route('/cart')
def cartpage():
    return render_template("cart.html")

# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
