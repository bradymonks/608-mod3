def maximum(n1,n2,n3):
    """Find max value of 3 numbers"""
    max_value = n1
    if n2 > max_value:
        max_value = n2
    if n3 > max_value:
        max_value = n3
    return max_value
### Brady Monks
print(maximum(12,27,36))

def minimum(n1,n2,n3):
    """Find the min value of 3 numbers"""
    min_value = n1
    if n2 < min_value:
        min_value = n2
    if n3 < min_value:
        min_value = n3
    return min_value
### Brady Monks
print(minimum(15,9,27))
