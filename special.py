"""Chef recently visited ShareChat Cafe and was highly impressed by the food. Being a food enthusiast, he decided to enquire about the ingredients of each dish.
There are N dishes represented by strings S1,S2,…,SN. Each ingredient used for making dishes in ShareChat Cafe is represented by a lowercase English letter. For each valid i, the ingredients used to make dish i correspond to characters in the string Si (note that ingredients may be used multiple times). A special ingredient is an ingredient which is present in each dish at least once.
Chef wants to know the number of special ingredients in ShareChat Cafe. Since Chef is too busy with work, can you help him?  """
try:
    t=int(input())
except:
    pass
for i in range(t):
    n=int(input())
    count=0
    arr=['a',0],['b',0],['c',0],['d',0],['e',0],['f',0],['g',0],['h',0],['i',0],['j',0],['k',0],['l',0],['m',0],['n',0],['o',0],['p',0],['q',0],['r',0],['s',0],['t',0],['u',0],['v',0],['w',0],['x',0],['y',0],['z',0]
    for j in range(n):
        st=input()
        for i in range(len(arr)):
            key=arr[i][0]
            for j in range(len(st)):
                if (key==st[j]):
                    arr[i][1]+=1
            
        for i in range(26):
            if arr[i][1]>=n:
                count+=1
    print(count)


