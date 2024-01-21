original_string = input()
target = input()

res = original_string
stack = []

for c in original_string:
    stack.append(c)
    if len(stack) >= len(target) and "".join(stack[-len(target) :]) == target:
        for _ in range(len(target)):
            stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")
