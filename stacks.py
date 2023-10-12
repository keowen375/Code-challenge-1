def is_balanced(expression):
    stack = []
    open_brackets = '([{'
    close_brackets = ')]}'
    

    for brac in expression:
        if brac in open_brackets:
            stack.append(brac)
        elif brac in close_brackets:
            if not stack:
                return False  
            first_brac = stack.pop()
            if open_brackets.index(first_brac) != close_brackets.index(brac):
                return False  

    return not stack 
            


expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  

