
a = int(input())

n = list(map(int, input().split()))

cnt = 0
c = 0

for i in n :
    if i == 0 :
        cnt -= n[c-1]
        if n[c-1] == 0 :
            cnt -= n[c-2]
    cnt += i
    c +=1

print(cnt)