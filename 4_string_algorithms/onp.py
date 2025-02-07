# Overall ONP which is in English - RPN (Reverse Polish Notation) is a form of notation that is used in mathematics
# and CS to calculate expressions, for example to write notation of 5 + 9 we do 5 9 +, it goes to the middle to make
# the equation
# Time complexity: O(n)
def onp(lst: list):
    # RNP uses stack method to 'store' expressions and bring it out if needed
    # for example when there's an equation to calculate
    # and also loop for looping through all items in the list, pretty self-explanatory
    stack = []
    for i in lst:
        # firstly we want to find if the item of the list is a digit so that we can convert it to int and
        # add it to a stack
        # if it's an operand like addition, subtraction, division or multiplication then we go to else and
        # pop out number b (at first because index for b number is higher than a) and then 'a' to, then make corresponding
        # equations (of course 'a' should be a leading number in subtraction and division to not mess up the equation)
        # multiplication and addition you can alternate through a or b, it'll be still the same
        # at the end pop out the most recent element in stack
        # (if the notation isn't wrote incorrectly, it should be the only element in stack)
        # to see the result
        if i.isdigit():
            n = int(i)
            stack.append(n)
        else:
            b = stack.pop()
            a = stack.pop()

            if i == '+':
                stack.append(b+a)
            elif i == '-':
                stack.append(a-b)
            elif i == '*':
                stack.append(b*a)
            else:
                stack.append(a//b)
    print(stack.pop())

onp(['5', '6', '8', '4', '*', '+', '/', '2', '+'])