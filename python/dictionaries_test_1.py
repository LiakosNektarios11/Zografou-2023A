transform={'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine"}
number=input("dwse enan arithmo ")
output=" "
for digit in number:
    output +=transform[digit] + " "
print(output)    
