import itertools
from fractions import Fraction

R = ((0, -1), (1, -1))

def matmul(A, B):
    return ((A[0][0]*B[0][0] + A[0][1]*B[1][0],
             A[0][0]*B[0][1] + A[0][1]*B[1][1]),
            (A[1][0]*B[0][0] + A[1][1]*B[1][0],
             A[1][0]*B[0][1] + A[1][1]*B[1][1]))

def det(M):
    return M[0][0]*M[1][1] - M[0][1]*M[1][0]

def scale(M, den):
    return tuple(tuple(Fraction(x, den) for x in row) for row in M)

# 深度搜索参数：分母扩展至27，元素范围扩展至±20
MAX = 20
DEPTHS = [0, 1, 2, 3]  # 分母为3^0,3^1,3^2,3^3 (即1,3,9,27)

candidates = []
for a11, a12, a21, a22 in itertools.product(range(-MAX, MAX+1), repeat=4):
    A = ((a11, a12), (a21, a22))
    if matmul(A, R) != matmul(R, A):
        continue
    for d in DEPTHS:
        denom = 3**d
        M = scale(A, denom)
        if det(M) not in (1, -1):
            continue
        maxabs = max(abs(x) for row in M for x in row)
        if maxabs <= 1:
            continue
        # 记录候选解及其行列式
        candidates.append((M, det(M)))

print(f"Total candidates found: {len(candidates)}")
if candidates:
    for idx, (M, det_val) in enumerate(candidates, 1):
        print(f"\nSolution {idx}:")
        print(f"[ {M[0][0]:<8} {M[0][1]:<8} ]")
        print(f"[ {M[1][0]:<8} {M[1][1]:<8} ]")
        print(f"Determinant: {det_val}")
        # 计算矩阵范数（最大行和范数）
        norm = max(abs(M[0][0]) + abs(M[0][1]), abs(M[1][0]) + abs(M[1][1]))
        print(f"Matrix norm: {norm}")
else:
    print("No non-trivial solutions found. This supports the uniqueness of k=3.")