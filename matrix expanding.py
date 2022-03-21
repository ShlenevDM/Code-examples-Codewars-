import numpy as np


def expand(maze, fill):
    return np.pad(np.array(maze, dtype=object), len(maze) // 2, 'constant', constant_values=fill)


mat = [[1, 1], [2, 2]]
print(expand(mat, 'aa'))
