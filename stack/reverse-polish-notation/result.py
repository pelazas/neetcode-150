class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        operators = ["*","+","-","/"]

        def perform_operation(num1,num2,op):
            if op == "*":
                return num1 * num2
            elif op == "/":
                return int(num1 / num2)
            elif op == "+":
                return num1 + num2
            elif op == "-":
                return num1 - num2

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                num = int(tokens[i])
                stack.append(num)
                print("push",num)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res_op = perform_operation(num1,num2,tokens[i])
                print(num1,tokens[i],num2,"=", res_op)
                stack.append(res_op)

        return stack.pop()
        