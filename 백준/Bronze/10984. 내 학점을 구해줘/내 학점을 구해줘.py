T = int(input())
for _ in range(T):
    N = int(input())
    c_t = 0
    g_a = 0 
    for _ in range(N):
        C, G = map(float, input().split())
        c_t += C
        g_a += C * G
    print(int(c_t), round(g_a/int(c_t), 1))