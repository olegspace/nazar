
pole_sansa=[["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"],
                ["*","*","*","*","*","*","*","*","*","*"]]
for stroka in pole_sansa:
    for kletka in stroka:    
        print(kletka,end=" ")
    print()
st=int(input("какой строка?\n"))
stal=int(input("какой столбец?\n"))
i = int(0)
j = int(0)

    
for stroka in pole_sansa:
    for kletka in stroka:
        kletka = "о"             
        print(kletka, end=" ")
                
print()
    
if(j != stal):
    j=j+1