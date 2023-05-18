email=input("dwse to email sou ")
x=email.index("@")

if '@' in email and email[-3: ] == ".gr" and email[x-1].isalpha() and email[x+1].isalpha():
        print(email)
else:
    print("akyro")
