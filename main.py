

class Stack:
    def __init__(self):
        self.stack = []

        
    
    def is_empty(self):
        print(self.stack)
        if self.stack:
            return True
        else:
            return False

    def stack_push(self, x):
        return self.stack.append(x)

    def stack_pop(self):
        return self.stack.pop()

    def stack_peek(self):
        return self.stack[-1]

    def stack_len(self):
        return len(self.stack)


def balance(x):
    s = Stack()
    for i in x:
        if i in '({[':
            s.stack_push(i)
        if i in ')}]':
            if not s.is_empty():
                return False
            else:
                t = s.stack_peek()
                if t == '{' or t == '[' or t == '(':
                    s.stack_pop()
                else:
                    return False
    return True

            
            
            




            

if __name__ == '__main__':
    lists = ['([{}])', '[([])((([[[]]])))]{()}', '{{[()]}}', '}{}', '{{[(])]}}', '[[{())}]']
    for x in lists:
        print(balance(x))






