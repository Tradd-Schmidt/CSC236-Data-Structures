class Explorer:
    def __init__(self, start_row, start_col):
        self.row = start_row
        self.col = start_col
        self.memory = [[self.row, self.col]]    # Will be used to log the places that the explorer has already been

    def move_n(self):
        self.row -= 1

    def move_s(self):
        self.row += 1

    def move_e(self):
        self.col += 1

    def move_w(self):
        self.col -= 1

    def remember(self, row=0, col=0):
        if row == 0 or col == 0:
            l = [self.row, self.col]
            self.memory.append(l)
        else:
            l = [self.row, self.col]
            self.memory.append(l)

    def print(self):
        print("(" + str(self.row) + "," + str(self.col) + ")")
