import unittest
from calculations import credit, payment, fullpayment, overprice

class Testcalculations(unittest.TestCase):
    def test_1(self):
        price = 40000       
        fpayment = 10000
        duration = 5
        percent = 13
        self.assertEqual(int(credit(price, fpayment)), 30000)
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 682)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 10955)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 40955)
    
    def test_2(self):
        price = 1638898      
        fpayment = 643489
        duration = 10
        percent = 17
        self.assertEqual(int(credit(price, fpayment)), 995409)
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 17299)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 1080587)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 2075996)

    def test_3(self):
        price = 2999999       
        fpayment = 500000
        duration = 20
        percent = 16.5
        self.assertEqual(int(credit(price, fpayment)), 2499999)
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 35722)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 6073401)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 8573400)
    def test_4(self):
        price = 100000000      
        fpayment = 20000000
        duration = 2
        percent = 21.4
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 4126586)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 19038081)
        self.assertEqual(int(credit(price, fpayment)), 80000000)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 99038081)
    def test_5(self):
        price = 1234       
        fpayment = 123
        duration = 100
        percent = 97.7
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 90)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 107433)
        self.assertEqual(int(credit(price, fpayment)), 1111)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 108544)
    def test_6(self):
        price = 40000       
        fpayment = 10000
        duration = 5
        percent = 13
        self.assertEqual(int(credit(price, fpayment)), 30000)
        self.assertEqual(int(payment(price, duration, percent, fpayment)), 682)
        self.assertEqual(int(overprice(duration, fpayment, price, percent)), 10955)
        self.assertEqual(int(fullpayment(duration, fpayment, percent, price)), 40955)
if __name__ == '__main__':
    unittest.main()