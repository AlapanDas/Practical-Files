import os

def make_commit(days:int):
    
    if days<1:
        return os.system('git push origin master -f \n 6969')
    else:
        dates=f'{days} days ago'
        with open('text.txt','a') as file:
            file.write(f'{dates}\n')
        
        os.system('git add text.txt')
        
        os.system('git commit --date="'+dates+'" -m "First Commit"')
        return days* make_commit(days-1)

make_commit(20)