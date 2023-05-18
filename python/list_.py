vathmos=input("Δώσε τον αριθμό πτυχίου σου ")
vathmos_1=float(vathmos)
if(vathmos_1 > 8.5 and vathmos_1 < 10 ):
    print("Άριστα")
elif(vathmos_1 >6.5 and vathmos_1 < 8.5):
    print("Πολύ καλά")
elif(vathmos_1 >= 5 and vathmos_1 < 6.5):
    print("Καλά")
else :
    print("Λάθος εισαγωγή")