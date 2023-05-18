ch=input("Θέλετε από (C)alsius σε Fahreneit ή από (F)ahreneit σε Calsius ? ")

if ch.upper()=='C' :
    tempC=input("Δώσε βαθμούς Κελσίου ")
    tempF=float(tempC) * 1.8 +32
    print(f" η θερμοκρασία σε Φάρεναιτ είναι {tempF} " )
elif ch.upper()=='F' :
    tempF=input("Δώσε βαθμούς Φάρεναιτ ")
    tempC=(float(tempF)-32)*5/9
    print(f"η θερμοκρασία σε Κελσίου είναι {tempC} ")  
else :
    print("Δεν είναι έγκυρη")



#f-32*5/9