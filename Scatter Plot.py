import matplotlib.pyplot as plt

x = [2, 5, 3, 4, 7, 5, 10, 11, 1, 6]

y = [3, 3, 4, 12, 5, 8, 7, 9, 10, 3]


plt.scatter(x,y, label= "dots", color ="red",
            marker = ".", s=70)

plt.xlabel('x')

plt.ylabel('y')

plt.title('Scatter Plot')

plt.legend()

plt.show()