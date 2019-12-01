#Currency Converter.
#USD => XAF  (Central African Francs)
#USD => NGN (Niara).
#200 >>>> Cameroon - XAF

def usd_xaf():
    send_amt = input("How much do you want to send? ")
    calc_amt = float(send_amt)*595.34
    print("Voila! " + send_amt + " in USD is " + str(calc_amt) + " in XAF")
def usd_ngn():
    send_amt = input("How much do you want to send? ")
    calc_amt = float(send_amt)*362.50
    print("Voila! " + send_amt + " in USD is " + str(calc_amt) + " in NGN")

print("Welcome to world currency converter!")
print("We are here to help you send money e.g. USD, XAF, NGN")

currency_source = input("Source currency: ")
currency_target = input("Target currency: ")

if currency_target == "XAF":
    usd_xaf()
elif currency_target == "NGN":
    usd_ngn()
else:
    print("Sorry! Currency currently not supported. Check back later.")


