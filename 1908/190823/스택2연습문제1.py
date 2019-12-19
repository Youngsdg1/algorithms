# ( 6 + 5 ) * ( 2 - 8 ) / 2
eq = list(input().split())
# icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}
# isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
stack = []
buho = []
for i in eq:
    if i != '/' and i != '*' and i != '+' and i != '-':
        stack.append(i)
        eq.remove(i)
    if i == '(' or i ==')':
        eq.remove(i)
for j in eq:
    stack.append(j)
print(stack)



# def postfix(eq):
#     for i in range(len(eq)):
#         for j in range(1, len(eq)):
#             if icp.keys(eq[i]) < icp.keys(j):
#                 stack.pop()
#             if icp.keys(eq[i]) > icp.keys(j):
#                 stack.append(eq[i])
#             else:
#                 result.append(eq[i])

