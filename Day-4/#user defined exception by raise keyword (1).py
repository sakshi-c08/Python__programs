#user defined exception by raise keyword
bank_bal = 500
if bank_bal<2000:
    raise Exception ("your account balance is below a accesing limit")
else:
    print("your amount has withdrawal")