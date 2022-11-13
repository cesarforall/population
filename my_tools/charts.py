import matplotlib.pyplot as plt


def print_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


def print_pie_chart(values, labels):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 500, 80]
    print_bar_chart(labels, values)
    # print_pie_chart(values, labels)
