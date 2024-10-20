def constant(inp):
    x = inp
    return x


def linear(inp):
    for i in inp:
        list_sum = list_sum + inp[i]
        
    return list_sum

def quadratic(inp):
    for i in range(inp):
        for j in range(inp):
            pass