class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        answer = ""
        
        for character in s:
            if character != ']':
                stack.append(character)
            else:
                parts= []
                while stack and stack[-1] != '[':
                    parts.append(stack.pop())
                stack.pop()
                digits = []
                while stack and stack[-1].isdigit():
                    digits.append(stack.pop())
                k = int("".join(reversed(digits)))
                stack.append(k*"".join(reversed(parts)))
        return "".join(stack)
        

