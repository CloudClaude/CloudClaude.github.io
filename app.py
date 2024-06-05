from flask import Flask, render_template, request
app = Flask(__name__)
import calculations

@app.route('/')
@app.route('/index')
def index():
  return render_template("index.html")

@app.route('/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
       price = float(request.form.get ('price'))
       fpayment = float(request.form.get ('fpayment'))
       duration = float(request.form.get ('duration'))
       percent = float(request.form.get ('percent'))

    credit = int(calculations.credit(price, fpayment))
    payment = int(calculations.payment(price, duration, percent, fpayment))
    fullpayment = int(calculations.fullpayment(duration, fpayment, percent, price))
    overprice = int(calculations.overprice(duration, fpayment, price, percent))

    return render_template("index.html", credit = credit, payment = payment, fullpayment = fullpayment, overprice = overprice)

@app.route('/about')
def about():
  return render_template("about.html")


if __name__ == "__main__":
  app.run(debug=True)