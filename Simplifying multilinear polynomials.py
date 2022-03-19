import re

poly = "a+ca-ab"

var = list(set([''.join(sorted(el)) for el in re.findall(r'[a-z]+', poly)]))
#print(var)

parsed = re.split('([+=-])', poly)
#print(parsed)

coefficients = {v:0 for v in var}
#print(coefficients)

for i in range(len(var)):
    for j in range(len(parsed)):
        #a = parsed[j].strip(var[i]) or 1
        if ''.join(sorted(parsed[j].lstrip('0123456789'))) == var[i] and parsed[j - 1] == '-':
            a = parsed[j].strip(var[i]) or 1
            coefficients[var[i]] -= int(a)
        elif ''.join(sorted(parsed[j].lstrip('0123456789'))) == var[i]:
            a = parsed[j].strip(var[i]) or 1
            coefficients[var[i]] += int(a)

print(coefficients)

sorted_variables = sorted(coefficients, key=lambda x: (len(x), x))
print(sorted_variables)
