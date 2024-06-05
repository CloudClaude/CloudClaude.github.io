def credit(price, fpayment):
    return price - fpayment
def payment(price, duration, percent, fpayment):
    return (price - fpayment) * (percent / 12 / 100) * (1 + (percent / 12 / 100))**(duration * 12) / ((1 + percent / 12 / 100)**(duration * 12) - 1)
def fullpayment(duration, fpayment, percent, price):
    return (price - fpayment) * (percent / 12 / 100) * (1 + (percent / 12 / 100))**(duration * 12) / ((1 + percent / 12 / 100)**(duration * 12) - 1) * duration * 12
def overprice(duration, fpayment, price, percent):
    return (price - fpayment) * (percent / 12 / 100) * (1 + (percent / 12 / 100))**(duration * 12) / ((1 + percent / 12 / 100)**(duration * 12) - 1) * duration * 12 + fpayment - price