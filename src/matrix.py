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
            return 'cannot multiply matrices'
        else:
            result = [[0 for x in range(new_matrix.num_cols)] for y in range(self.num_rows)]
            for i in range(len(result)):
                for j in range(len(result[i])):
                    for k in range(self.num_cols):
                        result[i][j] += self.elements[i][k] * new_matrix.elements[k][j]
            final = []
            for lst in result:
                final.append(lst)
            return Matrix(final)

    def get_smaller_matrix(self, i):
        if self.num_cols == 2 and self.num_rows == 2:
            return self.elements
        else:
            result = []
            for lst in self.elements:
                if self.elements.index(lst) != 0:
                    copy_lst = list(lst)
                    copy_lst.remove(lst[i])
                    result.append(copy_lst)
            return result

    def calc_determinant(self):
        if self.num_cols != self.num_rows:
            return 'cannot find determinant'
        if self.num_cols == 2 and self.num_rows == 2:
            result = self.elements[0][0] * self.elements[1][1] - self.elements[0][1] * self.elements[1][0]
        else:
            result = 0
            for i in range(len(self.elements[0])):
                item = self.elements[0][i]
                smaller_matrix = Matrix(self.get_smaller_matrix(i))
                result += (-1)**i * item * smaller_matrix.calc_determinant()
        return result
