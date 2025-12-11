raw = "AAAABBBCCDAA"

compressed = ""
cnt=0

for i in range(1, len(raw)):
    if raw[i]==raw[i-1]:
        cnt+=1
    else:
        compressed +=  str(cnt+1) + raw[i-1]
        cnt=0
        
compressed += str(cnt + 1) + raw[-1]
        
print(compressed)