class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val != '+' and val != '-' and val != '*' and val != '/':
                stack.append(int(val))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                print(num1, "", val, "", num2)
                if val == '+':
                    stack.append(int(num2 + num1))
                elif val == '-':
                    stack.append(int(num2 - num1))
                elif val == '*':
                    stack.append(int(num2 * num1))
                elif val == '/':
                    stack.append(int(num2 / num1))
        return stack[0]