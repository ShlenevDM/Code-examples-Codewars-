import re


def simplify(poly):
    var = list(set([''.join(sorted(el)) for el in re.findall(r'[a-z]+', poly)]))
    parsed = re.split('([+=-])', poly)
    coefficients = {v:0 for v in var}
    for i in range(len(var)):
        for j in range(len(parsed)):
            a = parsed[j].strip(var[i]) or 1
            if ''.join(sorted(parsed[j].lstrip('0123456789'))) == var[i] and parsed[j - 1] == '-':
                coefficients[var[i]] -= int(a)
            elif ''.join(sorted(parsed[j].lstrip('0123456789'))) == var[i]:
                coefficients[var[i]] += int(a)
    sorted_variables = sorted(coefficients, key=lambda x: (len(x), x))
    res = ""
    for v in sorted_variables:
        if coefficients[v] == 0:
            continue
        elif coefficients[v] == -1:
            res += '-' + str(v)
        elif coefficients[v] == 1:
            res += '+' + str(v)
        elif coefficients[v] < 0:
            res += f'-{abs(coefficients[v])}' + str(v)
        else:
            res += f'+{abs(coefficients[v])}' + str(v)
    res = res.lstrip('+')
    return res
