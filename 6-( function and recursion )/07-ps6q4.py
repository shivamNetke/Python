# waf to convert USD to INR

def converter(usdValue):
    inrValue = usdValue * 83
    print(usdValue, "USD =", inrValue, "INR")

converter(int(input("enter the value who's inr value you want to check : ")))