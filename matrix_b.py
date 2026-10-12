import torch
import time

def naive_matmul(A, B):
    n = len(A)

    C = [[0.0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C


sizes = [10, 20, 50, 100]

print("Matrix Size\tPyTorch Time (s)\tNaive Python Time (s)")
print("-" * 60)

for n in sizes:

    A = torch.randn(n, n)
    B = torch.randn(n, n)

    A_list = A.tolist()
    B_list = B.tolist()


    C = A @ B

    start = time.perf_counter()

    C = A @ B

    end = time.perf_counter()

    pytorch_time = end - start


    start = time.perf_counter()

    C_naive = naive_matmul(A_list, B_list)

    end = time.perf_counter()

    naive_time = end - start

    print(
        f"{n:4d}\t\t"
        f"{pytorch_time:.8f}\t\t"
        f"{naive_time:.8f}"
    )

    a=10
    b=11