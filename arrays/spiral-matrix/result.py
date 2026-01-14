class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        total_elements = len(matrix) * len(matrix[0])

        while len(output)< total_elements:

            for i in range (left, right+1):
                output.append(matrix[top][i])
            top +=1
            if len(output) == total_elements: break

            for i in range(top, bottom +1):
                output.append(matrix[i][right])
            right-=1
            if len(output) == total_elements: break
            
            for i in range(right, left-1,-1):
                output.append(matrix[bottom][i])
            bottom-=1
            if len(output) == total_elements: break

            for i in range(bottom, top-1,-1):
                output.append(matrix[i][left])
            left+=1
            if len(output) == total_elements: break

        return output
        
        