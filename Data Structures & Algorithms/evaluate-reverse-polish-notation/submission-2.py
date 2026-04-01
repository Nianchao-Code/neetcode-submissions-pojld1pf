class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t not in operations:
                stack.append(int(t))
                continue

            num1 = stack.pop()
            num2 = stack.pop()

            if t == "+":
                output = num2 + num1
            elif t == "-":
                output = num2 - num1
            elif t == "*":
                output = num2 * num1
            elif t == "/":
                output = int(num2 / num1)
            stack.append(output)

        return stack[0]
