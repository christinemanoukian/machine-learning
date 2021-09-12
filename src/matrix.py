class Matrix:
    def __init__(self, arr):
        self.elements = arr
        self.num_cols = len(arr[0])
        self.num_rows = len(arr)

    def print(self):
        for lst in self.elements:
            print(lst)

    def transpose(self):
        result = [[0 for x in range(self.num_rows)] for y in range(self.num_cols)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                result[i][j] = self.elements[j][i]
        return Matrix(result)

    def add(self, new_matrix):
        result = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                result[j][i] = self.elements[j][i] + new_matrix.elements[j][i]
        return Matrix(result)

    def subtract(self, new_matrix):
        result = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                result[j][i] = self.elements[j][i] - new_matrix.elements[j][i]
        return Matrix(result)

    def scalar_multiply(self, scalar):
        result = [[0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                result[j][i] = scalar * self.elements[j][i]
        return Matrix(result)

    def matrix_multiply(self, new_matrix):
        if self.num_cols != new_matrix.num_rows:
            print('cannot multiply matrices')
        else:
            result = [[0 for x in range(new_matrix.num_cols)] for y in range(self.num_rows)]
            for i in range(len(result)):
                for j in range(len(result[i])):
                    for k in range(self.num_cols):
                        result[i][j] += self.elements[i][k] * new_matrix.elements[k][j]
            for lst in result:
                print(lst)
