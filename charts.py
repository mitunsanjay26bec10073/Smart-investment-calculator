import matplotlib.pyplot as plt
import numpy as np

def dispPie(M, N):
    names = ['Invested Amount\n(' + str(format(N, ',d')) + ')',
             'Maturity Value\n(' + str(format(M, ',d')) + ')']
    pi = np.array([N, M])

    fig = plt.figure(figsize=(5, 5))

    plt.pie(pi, labels=names)
    plt.show()