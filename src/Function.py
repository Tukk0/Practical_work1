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

def remove_whtespaces(regex: str):
    new = ''
    for i in regex:
        if i != ' ':
            new += i
    return new

def number_of_operations(regex: str):
    cnt = 0
    for i in regex:
        if i in ['+', '*', '.']:
            cnt += 1
    return cnt

class Node:
    def __init__(self, value, prefix_possibility: bool, special_possibility: bool, special_length: int):
        self.value = value
        # Whether the special prefix can exist
        self.prefix_possibility = prefix_possibility
        # Whether the word can consist only of letter 'x'
        self.special_possibility = special_possibility
        # The max length of the prefix consisting only of letter 'x'
        self.special_length = special_length

def iterate(regex: str, letter, k: int):
    stack1 = list(regex)
    stack2 = []
    NodeList = []
    new = ''  # The regular expreesion in normal form
    error = ValueError("Incorrect regular expression presented")
    # Unwind the stack from the beginning
    while len(stack1) > 0:
        elem = stack1.pop(0)
        if elem in ['a', 'b', 'c']:
            stack2.insert(0, elem)
            prefix_p = False
            special_p = False
            special_l = 0
            if elem == letter:
                special_p = True
                special_l = 1
                if k == 1:
                    prefix_p = True
            node = Node(elem, prefix_p, special_p, special_l)
            NodeList.append(node)
        elif elem in ['.', '+']:
            if len(stack2) < 2:
                # Not enough elements to perform the operation
                raise error
            else:
                node2 = NodeList.pop()
                node1 = NodeList.pop()
                prefix_p = False
                special_p = False
                special_l = 0
                if elem == '.':
                    elem = ''
                    # Word 1 is of type "x...x"
                    if node1.special_possibility:
                        if node2.special_possibility:
                            special_p = True
                        special_l = node1.special_length + node2.special_length
                        if special_l >= k:
                            prefix_p = True
                    # Word1 is of type "x...xy..."
                    elif node1.special_length > 0:
                        special_l = node1.special_length
                        if special_l > k:
                            prefix_p = True
                # Get two elements and add or concatenate them in the order they are written
                new = stack2.pop(1) + elem + stack2.pop(0)
                # Get the last two elements
                if elem == '+':
                    if (node1.special_possibility or node2.special_possibility):
                        special_p = True
                    special_l = max(node1.special_length, node2.special_length)
                    if special_l >= k:
                        prefix_p = True
                    # Wrap the sum in brackets
                    new = '(' + new + ')'
                node = Node(elem, prefix_p, special_p, special_l)
                NodeList.append(node)
                stack2.insert(0, new)
        elif elem == '*':
            if len(stack2) < 1:
                # Not enough elements to perform the operation
                raise error
            else:
                node = NodeList.pop()
                prefix_p = False
                special_p = False
                special_l = 0
                if node.special_possibility:
                    special_p = True
                    prefix_p = True
                    special_l = k*node.special_length
                string = stack2.pop(0)
                if string[0] != '(' or string[-1] != ')':
                    # Wrap the result in brackets
                    new = ('(' + string + ')' + elem)
                else:
                    new = string + elem
                stack2.insert(0, new)
                node = Node(elem, prefix_p, special_p, special_l)
                NodeList.append(node)
    if len(stack2) != 1:
        # Not all elements are a part of the expression
        raise error
    return NodeList[0].prefix_possibility
    pass


def regex_has_a_special_prefix(regex: str, letter, k: int):
    print(regex_is_correct(regex))
    regex = remove_whtespaces(regex)
    print(regex)
    print(iterate(regex, letter, k))
    pass