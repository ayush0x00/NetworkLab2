import sys
import time

def pseudoLoop(n):
    while(n):
        n-=1

def main():
    loops = [1e3,1e4,1e5,1e6,1e7,1e8,1e9] 
    with open("data.txt","a") as f:
        for i in loops:
            start = time.time()
            print(f'loop {i} started\n')
            pseudoLoop(i)
            f.write(f'Time taken for n {i} is {time.time()-start}\n')
            print(f'loop {i} fininshed')

if __name__=="__main__":
    loops = sys.argv[1]
    if(loops):
        pseudoLoop(int(loops))
    else:
        main()