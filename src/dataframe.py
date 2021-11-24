class DataFrame:
    def __init__(self, data_dict, column_order):
        self.data_dict = data_dict
        self.column_order = column_order

    def to_array(self):
        result = []
        count = 0
        while count < len(self.data_dict.get(self.column_order[0])):
            row = []
            for name in self.column_order:
                row.append(self.data_dict[name][count])
            result.append(row)
            count += 1
        return result

    def select_columns(self, columns):
        new_dict = {}
        for key in columns:
            new_dict[key] = self.data_dict[key]
        return DataFrame(new_dict, columns)

    def select_rows(self, rows):
        new_dict = {}
        for key in self.column_order:
            new_lst = []
            for row in rows:
                value = self.data_dict.get(key)
                new_lst.append(value[row])
            new_dict[key] = new_lst
        return DataFrame(new_dict, self.column_order)

    @classmethod
    def from_array(cls, arr, column_order):
        data_dict = {}
        for i in range(len(column_order)):
            data_dict[column_order[i]] = []
            for lst in arr:
                data_dict[column_order[i]].append(lst[i])
        return cls(data_dict, column_order)

    def order_by(self, column, ascending):
        arr = self.to_array()
        col_ind = self.column_order.index(column)
        if ascending == True:
            arr.sort(key=lambda x: x[col_ind])
        if ascending == False:
            arr.sort(key=lambda x: x[col_ind], reverse=True)
        return DataFrame.from_array(arr, self.column_order)

    def to_json(self):
        new_lst = []
        for element in self.to_array():
            new_dict = {}
            for i in range(len(self.column_order)):
                new_dict[self.column_order[i]] = element[i]
            new_lst.append(new_dict)
        return new_lst

    @classmethod
    def from_json(cls, lst, column_order):
        data_dict = {}
        for column in column_order:
            data_dict[column] = []
            for dictionary in lst:
                data_dict[column].append(dictionary.get(column))
        return cls(data_dict, column_order)
