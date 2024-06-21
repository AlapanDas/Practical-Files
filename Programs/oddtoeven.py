n = int(input("Enter the size of the list "))
l = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
for i in len(l):
    if l[i]%2==0:
        continue
    else:
        l[i]*=2
print("CORRECTED LIST")
print(l)
def copy():
    file=open("file1.txt")
    c=file.readlines()
    file2=open("file2.txt",'w')
    file2.writelines(c)