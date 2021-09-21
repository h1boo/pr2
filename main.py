x=[5, 6, 7, 3, 4, 7, 160]
s=0
for i in range(5):
    a=x[i]
    for j in range(i+1, 5):
        b=x[j]
        for k in range(j+1, 5):
            c=x[k]
            if a+b>c and a+c>b and b+c>a:
                if a+b+c>s:
                    s=a+b+c
print(s)

