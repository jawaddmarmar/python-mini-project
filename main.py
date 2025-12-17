password = input("enter your password:")

def pwd_check(psd):
    res=""
    if len(psd) >=8:

        for x in psd:
            if x.isdigit():
                res="valid"
                print(res)
                return True
        res="must have a number"
        print(res)
    else:
        print("Your password is weak")

pwd_check(password)