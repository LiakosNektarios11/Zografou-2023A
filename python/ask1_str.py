onoma=input("Δώσε το όνομα σου")
name=onoma.replace("s","")
print("Γειά σου  " + name)
if name.find("s") == -1:
    new_name=name
else :
    new_name=name[:-1]
print(f"Καλημέρα {new_name}")

