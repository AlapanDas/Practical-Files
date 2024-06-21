# Calender App 1.0
#made by Alapan Das
database=[["1","New Year"],["12","Swami Vivekananda Jayanti"],["14","Makar Sankranti/Pongal"],["23","Netaji Subhas Chandra Bose Jayanti "],["26","Republic Day"]]
n=int(input("Enter your Day Number"))
m=int(input("Enter your month Number"))
if n>31 and m>12:
    print("Invalid Input")
for i in range(len(database)):
    if  m==1 :
        st= database[i][0]
        if n==int(st):
            print("Date is {} Jan and Holiday is {}".format(st,database[i][1]))
#end
