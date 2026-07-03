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
                num = ""
                while stack and stack[-1].isdigit():
                    num += stack.pop()
                k = int(num[::-1])
                stack.append(k*"".join(reversed(parts)))
        return "".join(stack)
        

