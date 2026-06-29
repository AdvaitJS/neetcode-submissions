class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for op in operations:
            if op not in "+DC":
                stack.append(int(op))
                total += int(op)
            elif op == "+":
                score = (stack[-1] + stack[-2])
                stack.append(score)
                total += score
            elif op == "D":
                total += (stack[-1]*2)
                stack.append(stack[-1]*2)
                
            elif op == "C":
                total -= stack[-1]
                stack.pop()
                
        return total 