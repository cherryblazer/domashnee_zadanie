class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def __str__(self):
        res = ""
        for i in self.arr:
            res += str(i) + '\n';
        return res

    def __add__(self, second):
        new = []
        for i in range(len(self.arr)):
            temp = []
            for j in range(len(self.arr[i])):
                temp.append(self.arr[i][j] + second.arr[i][j])
            new.append(temp)
        return Matrix(new);