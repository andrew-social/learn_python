# Calculates sequence of prime numbers from min to max
# Prints list in ordered columns
# prompts for minimun, and maximun numbers

import math

def list_columns(obj, cols=4, columnwise=True, gap=4):
    """
    Print the given list in evenly-spaced columns.

    Parameters
    ----------
    obj : list
        The list to be printed.
    cols : int
        The number of columns in which the list should be printed.
    columnwise : bool, default=True
        If True, the items in the list will be printed column-wise.
        If False the items in the list will be printed row-wise.
    gap : int
        The number of spaces that should separate the longest column
        item/s from the next column. This is the effective spacing
        between columns based on the maximum len() of the list items.
    Examples: 
    	list_columns(foolist)
    	list_columns(foolist, cols=2)
    	list_columns(foolist, columnwise=False)
    	list_columns(foolist, gap=1)
    """

    sobj = [str(item) for item in obj]
    if cols > len(sobj): cols = len(sobj)
    max_len = max([len(item) for item in sobj])
    if columnwise: cols = int(math.ceil(float(len(sobj)) / float(cols)))
    plist = [sobj[i: i+cols] for i in range(0, len(sobj), cols)]
    if columnwise:
        if not len(plist[-1]) == cols:
            plist[-1].extend(['']*(len(sobj) - len(plist[-1])))
        plist = zip(*plist)
    printer = '\n'.join([
        ''.join([c.ljust(max_len + gap) for c in p])
        for p in plist])
    print(printer)

def input_num(prompt="Enter a number: "):
    """
    prompt the user for a numeric input
    prompt again if the input is not numeric
    return an integer or a float
    """
    while True:
        # strip() removes any leading or trailing whitespace
        num_str = input(prompt).strip()
        num_flag = True
        for c in num_str:
            # check for non-numerics
            if c not in '+-.0123456789':
                num_flag = False
        if num_flag:
            break
    # a float contains a period (US)
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)
#    return int(num_str)

def input_num2(prompt="Enter a number: "):
    """
    prompt the user for a numeric input
    prompt again if the input is not numeric
    return an integer or a float
    """
    while True:
        # strip() removes any leading or trailing whitespace
        num_str = input(prompt).strip()
        # make sure that all char can be in a typical number
        if all(c in '+-.0123456789' for c in num_str):
            break
    # a float contains a period (US)
    if '.' in num_str:
        return float(num_str)
    else:
        return int(num_str)
# test ...
#num = input_num()
#print(type(num))
#print(num)
#print('-'*20)
#num2 = input_num2()
#print(type(num2))
#print(num2)

def is_prime(start = 2, end = 999):
# Python program to print all  
# prime number in an interval 
  
	result=[]
	for val in range(start, end + 1):
		for n in range(2, val): 
			if (val % n) == 0:
				break
		else:
			result.append(val)
#	print(result)
	return(result)

start = input_num('Enter a begining integer: ')
end = input_num('Enter an ending integer: ')
result = is_prime(start, end)

list_columns(result, cols=20, columnwise=False)

