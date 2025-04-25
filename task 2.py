try:
    org_list = []
    n = int(input('Enter a number for range of list : '))
    for i in range(1,n+1):
        org_list.append(i)
    print(f"Original list = {org_list}")
    if n % 2 == 0 :
        num1 = n//2
    else:
        num1 = (n+1)//2
    numm =int(num1)

    slcd_list = org_list[:numm]
    print(f"extracted first {num1} elements = {slcd_list}")
    reversedlist = slcd_list.reverse()
    print(f"Reversed extracted elements = {slcd_list}")

except ValueError :
    print(f"Please enter an integer ")


