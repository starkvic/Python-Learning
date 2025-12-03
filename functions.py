def tri_recurs(k):
    if(k>0):
        result = k +tri_recurs(k-1)
        print(result)
    else:
        result = 0
    return result
print("Recursion example results")
tri_recurs(6)

def factorial_func(k):
    if k==0:
    	return 1
    else:
        result = k*factorial_func(k-1)
    print(result)
    return result

print("the factorial is",factorial_func(15))

