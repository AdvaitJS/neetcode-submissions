class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op not in "+DC":
                stack.append(int(op))
            elif op == "+":
                a , b = stack[-1] , stack[-2]
                stack.append(a+b)
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "C":
                stack.pop()
        return sum(stack) 