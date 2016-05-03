def adress():
    import matplotlib
    import matplotlib.pyplot as plt

    word = 'Hongji 2gil 20,Jongrogu,Seoul'

    H=dict()
    H['str']=0
    H['int']=0
    for i in word:
        if i.isalpha():
                H['str']=H['str']+1
        elif i.isdigit:
                H['int']=H['int']+1
    print H


    plt.bar(range(len(H)),H.values(),align='center')
    plt.xticks(range(len(H)),list(H.keys()))
    plt.show()

adress()