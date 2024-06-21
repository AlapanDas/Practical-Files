def LSP(arr, n):
	count = [0 for i in range(n + 1)]
	for i in range(n):
		count[arr[i]] += 1
	key = 1
	copy = 0
	vis = [0 for i in range(n + 1)]
	for i in range(n):
		if (count[arr[i]] == 1):
			continue
		while (count[key]):
			key += 1
		if (key > arr[i] and vis[arr[i]] == 0):
			vis[arr[i]] = 1 
		else:
			count[arr[i]] -= 1
			arr[i] = key
			copy += 1
			key += 1
	
	print(copy)
	for i in range(n):
		print(arr[i], end = " ")

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(int(input()))
        LSP(arr,n)