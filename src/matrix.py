class Matrix:
    def __init__(self, arr):
        self.elements = arr
        self.num_cols = len(arr[0])
        self.num_rows = len(arr)

    def __add__(self, other):
        return self.add(other)
    
    def __sub__(self, other):
        return self.subtract(other)
    
    def __mul__(self, scalar):
        return self.scalar_multiply(scalar)

    def __rmul__(self, scalar):
        return self.scalar_multiply(scalar)

    def __matmul__(self, other):
        return self.matrix_multiply(other)
    
    def __pow__(self, exp):
        return self.exponent(exp)

    def __eq__(self, other):
        return self.elements == other.elements

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

    def identity(self):
        result = [[0.0 for x in range(self.num_cols)] for y in range(self.num_rows)]
        x = 0
        i = 0
        while x >= 0 and i >= 0:
            if x == self.num_rows or i == self.num_cols:
                break
            else:
                result[x][i] += 1.0
                x += 1
                i += 1
        return Matrix(result)

    def combine(self):
        left_side = self.copy()
        left = left_side.elements
        right_side = left_side.identity()
        result = []
        for i in range(len(left)):
            result.append(left[i] + right_side.elements[i])
        return Matrix(result)

    def take_apart(self):
        end = self.num_rows
        right_side = []
        for i in range(self.num_rows):
            right_side.append(self.elements[i][end:])
        return Matrix(right_side)

    def inverse(self):
        if self.num_rows != self.num_cols:
            return 'no inverse'
        elif self.calc_determinant() == 0:
            return 'no inverse'
        else:
            result = self.copy()
            result = result.combine()
            result = result.rref()
            result = result.take_apart()
            return result

    def determinant_by_rref(self):
        if self.num_rows != self.num_cols:
            return 'no determinant'
        elif self.rref().elements != self.identity().elements:
            return 0
        else:
            result = self.copy()
            row_ind = 0
            swap_rows_count = 0
            scaling_factor_count = 1
            for col_ind in range(result.num_cols):
                pivot_row = result.get_pivot_row(col_ind)
                if pivot_row is not None:
                    if pivot_row != row_ind:
                        result = result.swap_rows(row_ind, pivot_row)
                        swap_rows_count += 1
                    scaling_factor_count *= result.elements[row_ind][col_ind]
                    result = result.make_value_one(row_ind)
                    result = result.make_above_zero(row_ind)
                    result = result.make_below_zero(row_ind)
                    row_ind += 1
            sign = (-1) ** swap_rows_count
            return int(sign * scaling_factor_count)
    
    def exponent(self, exp):
        answer = Matrix(self.elements)
        if answer.num_cols != answer.num_rows:
            print("doesn't work")
        else:
            while exp > 1:
                answer = answer.matrix_multiply(Matrix(self.elements))
                exp -= 1
            return answer
