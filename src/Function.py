def regex_is_correct(regex: str):
    stack1 = list(regex)
    stack2 = []
    new = ''
    while len(stack1) > 0:
        elem = stack1.pop(0)
        if elem == ' ':
            continue
        elif elem in ['a', 'b', 'c']:
            stack2.insert(0, elem)
        elif elem in ['.', '+']:
            if len(stack2) < 2:
                raise ValueError("Incorrect regular expression presented")
            else:
                if elem == '.':
                    elem = ''
                # Get two elements and add or concatenate them
                new = stack2.pop(1) + elem + stack2.pop(0)
                if elem == '+':
                    new = '(' + new + ')'
                stack2.insert(0, new)
        elif elem == '*':
            if len(stack2) < 1:
                raise ValueError("Incorrect regular expression presented")
            else:
                string = stack2.pop(0)
                if string[0] != '(' or string[-1] != ')':
                    new = ('(' + string + ')' + elem)
                else:
                    new = string + elem
                stack2.insert(0, new)
        else:
            raise ValueError("Incorrect regular expression presented")
    if len(stack2) != 1:
        raise ValueError("Incorrect regular expression presented")
    return new
    #raise NotImplementedError("Not implemented")

def function(regex: str, x, k: int):
    regex_is_correct(regex)
    pass