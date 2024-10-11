def regex_is_correct(regex: str):
    stack1 = list(regex)
    stack2 = []
    new = ''
    error = ValueError("Incorrect regular expression presented")
    # Unwind the stack from the beginning
    while len(stack1) > 0:
        elem = stack1.pop(0)
        if elem == ' ':
            continue
        elif elem in ['a', 'b', 'c']:
            stack2.insert(0, elem)
        elif elem in ['.', '+']:
            if len(stack2) < 2:
                # Not enough elements to perform the operation
                raise error
            else:
                if elem == '.':
                    elem = ''
                # Get two elements and add or concatenate them in the order they are written
                new = stack2.pop(1) + elem + stack2.pop(0)
                if elem == '+':
                    # Wrap the sum in brackets
                    new = '(' + new + ')'
                stack2.insert(0, new)
        elif elem == '*':
            if len(stack2) < 1:
                # Not enough elements to perform the operation
                raise error
            else:
                string = stack2.pop(0)
                if string[0] != '(' or string[-1] != ')':
                    # Wrap the result in brackets
                    new = ('(' + string + ')' + elem)
                else:
                    new = string + elem
                stack2.insert(0, new)
        else:
            raise error
    if len(stack2) != 1:
        # Not all elements are a part of the expression
        raise error
    return new

def regex_has_a_special_prefix(regex: str, x, k: int):
    regex_is_correct(regex)
    pass
