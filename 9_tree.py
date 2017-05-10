class Tree:
    def __init__(self, value=None):
        self.value = value
        self.left = self.right = None

    def push(self, value):
        if self.value is None:
            self.value = value
        elif value > self.value:
            if self.right is None:
                self.right = Tree(value)
            else:
                self.right.push(value)
        else:
            if self.left is None:
                self.left = Tree(value)
            else:
                self.left.push(value)

    def find_path_sum(self):
        queue = [(self, 0)]
        min_time = None
        while queue:
            current, time = queue.pop(0)
            if min_time == current.left == current.right is None:
                min_time = time
            else:
                if current.left is not None:
                    queue.append((current.left, time + 1))
                if current.right is not None:
                    queue.append((current.right, time + 1))
        return min_time + time


my_tree = Tree()
for elem in list(map(int, input().split())):
    my_tree.push(elem)
print(my_tree.find_path_sum())
