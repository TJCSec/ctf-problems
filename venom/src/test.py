s = open("final2.bf").read().split('\n')
bo = [[i for i in j] for j in s]
#for i in bo:
#    print(len(i))
x = 0
y = 0
d = 0
# right, left, down, up
d2 = [(1,0),(-1,0),(0,1),(0,-1)]
ii = 0
quote = False
st = [[0 for i in range(2000)] for j in range(3)]
sti = 0
esp = [0,0,0]
inp = [ord(i) for i in 'b4s1cally_bal3ful_plu5_plu5']
ip = 0

# esp is next empty slot

while True:
    c = bo[y][x]
    if c == '"':
        quote = not quote
    elif quote:
        st[sti][esp[sti]] = ord(c)
        esp[sti] += 1
    elif c == '>':
        d = 0
    elif c == '<':
        d = 1
    elif c == 'v':
        d = 2
    elif c == '^':
        d = 3
    elif c == 'j':
        sti += 1
    elif c in '0123456789':
        st[sti][esp[sti]] = ord(c)-ord('0')  
        esp[sti] += 1      
    elif c == 'g':
        esp[sti] -= 1
        pos = st[sti][esp[sti]]
        esp[sti] -= 1
        num = st[sti][esp[sti]]
        st[sti][esp[sti]] = st[num][pos]
        esp[sti] += 1
        print("get",st[num][pos],num,pos)
    elif c == 's':
        esp[sti] -= 1
        val = st[sti][esp[sti]]
        esp[sti] -= 1
        pos = st[sti][esp[sti]]
        esp[sti] -= 1
        num = st[sti][esp[sti]]
        st[num][pos] = val
        print("store",val,num,pos)
    elif c == 'p':
        esp[sti] -= 1
    elif c == 'm':
        st[sti][esp[sti]-1] %= 256
    elif c == 'n':
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        st[sti][esp[sti]] = 0b1111111111111111 - (a|b)
        esp[sti] += 1
    elif c == '-':
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        st[sti][esp[sti]] = b-a
        esp[sti] += 1
    elif c == '+':
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        st[sti][esp[sti]] = b+a
        esp[sti] += 1
    elif c == '*':
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        st[sti][esp[sti]] = b*a
        esp[sti] += 1
        input()
    elif c == 'c':
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        st[sti][esp[sti]] = b^a
        esp[sti] += 1
    elif c == 'i':
        st[sti][esp[sti]] = inp[ip]
        ip += 1
        esp[sti] += 1
    elif c == '|':
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        if a>b:
            d = 2
        elif a<b:
            d = 3
    elif c == '_':
        esp[sti] -= 1
        b = st[sti][esp[sti]]
        esp[sti] -= 1
        a = st[sti][esp[sti]]
        print("_",a,b,d)
        if a>b:
            d = 0
        elif a<b:
            d = 1
    elif c == 'r':
        esp[sti] -= 1
        print("Return:",st[sti][esp[sti]])
        break
    elif c == ' ':
        pass
    elif c == '?':
        pass
    else:
        print("unknown:",c)
    x += d2[d][0]
    y += d2[d][1]
    print(x,y,hex(ord(c)),d,c,ii,esp,st[1][:min(max(st[2][0],0),10)],st[2][:min(max(esp[2],0),10)])
