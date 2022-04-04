class NotValidInput(Exception):
    pass


def validate_brackets(Stack, string) -> bool:
    if type(string) != str:
        raise NotValidInput('Your input is not valid!')
    stack = Stack()
    closed = ''
    for i in string:
        if i == '(' or i == '[' or i == '{':
            stack.push(i)
            closed = get_closed_bracket(i)
            continue

        if i == ')' or i == ']' or i == '}':
            if closed == i:
                stack.pop()
                closed = get_closed_bracket(stack.peek())

    if stack.is_empty():
        return True
    return False


def get_closed_bracket(open_bracket):
    if open_bracket == '(':
        return ')'
    if open_bracket == '[':
        return ']'
    if open_bracket == '{':
        return '}'


if __name__ == "__main__":
    from stack_and_queue import Stack
    string = '{(})'
    string = 1
    print(validate_brackets(Stack, string))
