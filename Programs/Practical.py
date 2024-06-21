def potential():
    st=input("Enter sentence")
    st.upper()
    l=[]
    sent=""
    if st[-1] in ['.','!','?']:
        st=st[:-1]
        l=st.split()
    for i in l:
        sent+=str(l)+" "
    key=input("WORD TO BE DELETED")
    pos=int(input("WORD TO BE DELETED"))
    if l[pos-1]==key:
        l.remove(key)
        sent=""
    else:
        print("invalid input")
    for i in l:
        sent+=str(l)+" "
    print(sent)
potential()