import sys
input=sys.stdin.readline

N,K=map(int,input().split())
arr=list(map(int,input().split()))

left,right=0,0
check=[0]*100001
answer=0
cnt=0
while right<N:
    if check[arr[right]]<K:
        check[arr[right]]+=1
        cnt+=1
        right += 1
    else:
        answer=max(answer,cnt)
        cnt-=1
        check[arr[left]]-=1
        left+=1
answer=max(answer,cnt)
print(answer)