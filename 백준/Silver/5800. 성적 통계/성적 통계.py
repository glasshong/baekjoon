K = int(input())
l = []
for i in range(K):
    l = list(map(int, input().split()))
    l = sorted(l[1:])
    print(f'Class {i+1}', f'Max {max(l)}, Min {min(l)}, Largest gap {max(l[i+1]-l[i] for i in range(len(l)-1))}', sep='\n')