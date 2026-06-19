class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in "+-/*":
                a , b = stack.pop() , stack.pop()
                if i == "+":res = int(a) + int(b)
                elif i == "-":res = int(b) - int(a)
                elif i == "*":res = int(a) * int(b)
                else: res = int(int(b) / int(a))
                stack.append(str(res))
            else: stack.append(i)
        return int(stack.pop())