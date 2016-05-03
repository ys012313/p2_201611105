def charCount():
    sel1=raw_input("Word?:")
    H=dict()
    word=sel1
    for c in word:
        if c not in H:
            H[c]=1
        else:
            H[c]=H[c]+1
    print H
    import matplotlib
    import matplotlib.pyplot as plt

    plt.bar(range(len(H)),H.values(),align='center')
    plt.xticks(range(len(H)),list(H.keys()))
    plt.show()

charCount()