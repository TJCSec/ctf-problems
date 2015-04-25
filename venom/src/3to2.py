# opcodes:
# push val
#   push val onto the stack
# get val
#   push value at val onto the stack
# store val
#   pop value, store at val
# nor
#   nor two top (universal gate)
# add
#   add two top
# mult
#   multiply two top
# ret
#   stop and return value
# cmp val
#   set zero flag to comparison
# input
#   push input byte onto the stack
# mod
#   mod by 256

d = {
'push':'\x00',
'get':'\x01',
'store':'\x02',
'nor':'\x03',
'add':'\x04',
'mult':'\x05',
'ret':'\x06',
'cmp':'\x07',
'input':'\x08',
'mod':'\x09'}

'''
push 42
push 57
push 49

# for i in [72, 191, 87, 4, 157, 222, 212, 69, 43, 44, 174, 252, 74, 148, 6, 228, 22, 4, 4, 105, 59, 186, 87, 137, 206, 54, 41]
input
get 0
get 0
nor
get 4
get 4
nor
nor
get 0
get 4
nor
nor
cmp i

# ???
get 3
nor
get 5
nor
store 3
store 4 # pop
# ???

get 0
get 1
mult
get 2
add
store 0

ret'''

code = ''
code += d['push']+chr(42)
code += d['push']+chr(57)
code += d['push']+chr(49)
code += d['push']+chr(0)

for i in [72, 191, 87, 4, 157, 222, 212, 69, 43, 44, 174, 252, 74, 148, 6, 228, 22, 4, 4, 105, 59, 186, 87, 137, 206, 54, 41]:
    code += d['input']
    code += d['get']+chr(0)
    code += d['get']+chr(0)
    code += d['nor']
    code += d['get']+chr(4)
    code += d['get']+chr(4)
    code += d['nor']
    code += d['nor']
    code += d['get']+chr(0)
    code += d['get']+chr(4)
    code += d['nor']
    code += d['nor']
    code += d['cmp']+chr(i)

    code += d['get']+chr(3)
    code += d['nor']
    code += d['get']+chr(5)
    code += d['nor']
    code += d['store']+chr(3)
    code += d['store']+chr(4)

    code += d['get']+chr(0)
    code += d['get']+chr(1)
    code += d['mult']
    code += d['get']+chr(2)
    code += d['add']
    code += d['mod']
    code += d['store']+chr(0)

code += d['ret']
print(code)
print([ord(i) for i in code])
print(len(code))
