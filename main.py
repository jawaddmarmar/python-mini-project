password = input("enter your password:")

def pwd_check(psd):
    has_number = False
    has_uppercase = False
    has_special=False
    specials="!@#$%^&*?"
    if len(psd) >=8:

        for x in psd:
            if x.isdigit():
                has_number=True

################################
                          
            if x.isupper():
                has_uppercase=True

###############################                

            if x in specials:
                has_special=True

###############################                
        if has_number and has_uppercase and has_special:
            print("strong")    
        elif has_number or has_uppercase or has_special:   
            print("medium") 
        else:
            print("weak")
            
    else:
        print("Your password is weak")

pwd_check(password)