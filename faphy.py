import numpy as np

def get_weights():
    # random consistency index (RI)
    RI = [0, 0, 0.58, 0.90, 1.12, 1.24, 1.32, 1.41, 1.45, 1.49, 1.51, 1.48, 1.56, 1.57, 1.59]

    # read pairwise matrix # TODO: do it need to change to file and then input?!
    c = np.array([[1, 6, 1 / 4, 2, 3, 3, 4, 1 / 4, 2, 1 / 2, 5, 1, 1 / 4],
                  [0, 1, 1 / 9, 1 / 5, 1 / 4, 1 / 4, 1 / 3, 1 / 9, 1 / 5, 1 / 7, 1 / 2, 1 / 6, 1 / 9],
                  [0, 0, 1, 5, 6, 6, 7, 2, 5, 3, 8, 4, 2],
                  [0, 0, 0, 1, 2, 2, 3, 1 / 5, 1, 1 / 3, 4, 1 / 2, 1 / 5],
                  [0, 0, 0, 0, 1, 1, 2, 1 / 6, 1 / 2, 1 / 4, 3, 1 / 3, 1 / 6],
                  [0, 0, 0, 0, 0, 1, 2, 1 / 6, 1 / 2, 1 / 4, 3, 1 / 3, 1 / 6],
                  [0, 0, 0, 0, 0, 0, 1, 1 / 7, 1 / 3, 1 / 5, 2, 1 / 4, 1 / 7],
                  [0, 0, 0, 0, 0, 0, 0, 1, 5, 3, 8, 4, 1],
                  [0, 0, 0, 0, 0, 0, 0, 0, 1, 1 / 3, 4, 1 / 2, 1 / 5],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 2, 1 / 3],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 / 5, 1 / 8],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1 / 4],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
    data = c
    n = len(data)
    A = np.reshape(data, (n, n))

    # complete inferior part with inverse values 1/x
    for a in range(len(A)):
        for b in range(len(A)):
            if a > b:
                A[a][b] = 1./A[b][a]
    A[A > 1] = np.round(A[A > 1]); A[A < 1] = np.round(A[A < 1], 3) # Round values
    # print('Decision Matrix:\n', A)

    # Eigenvalue
    alpha = A.sum(axis=0)
    w = alpha / A.sum()
    # print('\nWeights:\n', w.round(4))

    # Consistency ratio calculation
    maxvalue=w*alpha
    maxvalue2=maxvalue.sum(axis=0)
    #print("\nmaxval:\n",maxvalue2)
    CI = (maxvalue2-n)/(n-1)
    CR = CI/RI[n-1]
    # print ("\nConsistency Ratio:", CR)


    # write file
    with open('data/weights', 'w') as f:
        for item in w:
            f.write(str(item) + ' ')
    return w