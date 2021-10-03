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

    def copy(self):
        result = [[num for num in row] for row in self.elements]
        return Matrix(result)

    def get_pivot_row(self, col_ind):
        for row in range(self.num_rows):
            initial = True
            for i in range(col_ind):
                if self.elements[row][i] != 0:
                    initial = False
            if self.elements[row][col_ind] != 0 and initial:
                return row
        return None

    def swap_rows(self, row1, row2):
        result = self.copy()
        result.elements[row1], result.elements[row2] = result.elements[row2], result.elements[row1]
        return result

    def num_not_zero(self, row_ind):
        for i in range(self.num_cols):
            num = self.elements[row_ind][i]
            if num != 0:
                return num

    def make_value_one(self, row_ind):
        result = self.copy()
        column = result.num_not_zero(row_ind)
        for i in range(len(result.elements[row_ind])):
            result.elements[row_ind][i] = result.elements[row_ind][i] / column
        return result

    def ind_not_zero(self, row_ind):
        for i in range(self.num_cols):
            if self.elements[row_ind][i] != 0:
                return i

    def make_below_zero(self, row_ind):
        result = self.copy()
        ind = result.ind_not_zero(row_ind)
        num = result.num_not_zero(ind)
        for row in result.elements[row_ind + 1:]:
            multiplying_num = row[ind] / result.elements[row_ind][ind]
            for i in range(result.num_cols):
                row[i] -= multiplying_num * result.elements[row_ind][i]
        return result

    def make_above_zero(self, row_ind):
        result = self.copy()
        ind = result.ind_not_zero(row_ind)
        num = result.num_not_zero(ind)
        for row in result.elements[:row_ind]:
            multiplying_num = row[ind] / result.elements[row_ind][ind]
            for i in range(result.num_cols):
                row[i] -= multiplying_num * result.elements[row_ind][i]
        return result

    def rref(self):
        result = self.copy()
        row_ind = 0
        for col_ind in range(result.num_cols):
            pivot_row = result.get_pivot_row(col_ind)
            if pivot_row is not None:
                if pivot_row != row_ind:
                    result = result.swap_rows(row_ind, pivot_row)
                result = result.make_value_one(row_ind)
                result = result.make_above_zero(row_ind)
                result = result.make_below_zero(row_ind)
                row_ind += 1
        return result
