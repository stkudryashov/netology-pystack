class PyStack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


pairs = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def check_brackets(string: str) -> str:
    brackets = PyStack()

    for item in string:
        if item in ('(', '[', '{'):
            brackets.push(item)
            continue

        if item in (')', ']', '}'):
            if brackets.isEmpty():
                return 'Несбалансированно'
            else:
                if item != pairs.get(brackets.pop()):
                    return 'Несбалансированно'

    if brackets.isEmpty():
        return 'Сбалансированно'
    else:
        return 'Несбалансированно'


if __name__ == '__main__':
    result = check_brackets(input('Ваша строка -> '))
    print(result)
