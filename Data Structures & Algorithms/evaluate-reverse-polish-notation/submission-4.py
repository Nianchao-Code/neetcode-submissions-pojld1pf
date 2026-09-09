class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        set_op = {"+", "-", "*", "/"}

        for char in tokens:
            if char not in set_op:
                stack.append(int(char))

            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if char == "+":
                    num = num2 + num1
                if char == "*":
                    num = num2 * num1
                if char == "-":
                    num = num2 - num1
                if char == "/":
                    num = int(num2 / num1)

                stack.append(num)

        return stack[0]