global data
def database(n):
        data={1:"Hydrogen 1",
            2:"Helium 4",
            3:"Lithium 9",
            4:"Berylium 9",
            5:"Boron 11",
            6:"Carbon 12",
            7:"Nitrogen 14",
            8:"Oxygen 16",
            9:"Flourine 19",
            10:"Neon 20"     }
        return data.get(n)
        
def askup():
        n=int(input("Enter Atomic Number"))
        print(database(n))

if __name__=='__main__':
    for i in range(0,3):
        askup()
