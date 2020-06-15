
# %% [markdown]
# It's a sorting algorith, which transport's the values on each itteration

# %% [markdown]
# Intial list
# %% [codecell]

L = [13, 40, 50, 50, 90, 18, 30, 50, 30, 70]

# %% [markdown]
# List length:
# %% [codecell]
N = len(L)

# %% [markdown]
# <ln> 1) We write the range(N-1) which will return also the value N-2 as it's <br>
#        described by the pseudocode.</ln></br>
# 2) We write the range(N-1-i) which will retrun also the value N-2-i.<br>
# 3) If we want the sorting to be in descenting order we pass the conditional<br>
#        as 'if L\[j+1\] > L\[j\]' <br>
# 4) For the tansportation a temporary variable is not required.

# %% [codecell]
for i in range(N-1):  # 1
    for j in range(N-1-i):  # 2
        print(f'i:{i}, j:{j}, L[{j}]:{L[j]}, L[{j+1}]:{L[j+1]} ')
        print(L)
        if L[j+1] < L[j]:  # 3
            L[j], L[j+1] = L[j+1] , L[j]  # 4

# %% [markdown]
# Our sorted list is:
# %% [codecell]
L
