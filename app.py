def maximum_moment(time: str) -> str:

        l=time.split(':')
        temp=""
        i=l[0]
        if(i[0]=='?' and i[1]!='?'): temp+='2'+i[1]
        elif(i[0]!='?' and i[1]=='?'):temp=i[0]+'3'
        elif(i[0]=='?' and i[1]=='?'):temp="23"
        else:
            temp=i
        s=temp+":"
        i=l[1]
        if(i[0]=='?' and i[1]!='?'): temp='5'+i[1]
        elif(i[0]!='?' and i[1]=='?'):temp=i[0]+'9'
        elif(i[0]=='?' and i[1]=='?'):temp="59"
        else:
            temp=i
        s+=temp
        return s
print(maximum_moment("2?:00"))