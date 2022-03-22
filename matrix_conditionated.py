import numpy as np

def matrix_conditionated(len_i:int, len_j:int, cond_ops:dict) -> list:
    def conditions(i, j):
        for cond , op in cond_ops.items():
            if cond(i, j):
                return op(i, j)
        else:
            return 0
    return np.array([conditions(i, j) for i in range(1, len_i+1) for j in range(1, len_j+1)]).reshape((len_i, len_j))

#TRYOUTS
cd = {(lambda x, y:x==y):(lambda x, y:x+y),
      (lambda x, y:x>y):(lambda x, y: 2*x),
      (lambda x, y:x<y):(lambda x, y: x**2-y)}

print(matrix_conditionated(5, 6, cd))


