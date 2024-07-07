import matplotlib.pyplot as plt


student = [1, 2, 3, 4, 5]

height = [ 50, 11, 36, 25, 23]

tick_label = ['Daivd', 'Tony', 'Henry',  'Leo', 'Bohdan']

plt.bar(student, height, tick_label = tick_label,
        width = 0.8, color = ['orange', 'red', 'green', 'gray', 'purple'])

plt.xlabel('Name of Students')

plt.ylabel('Height of Students')

plt.title('Students vs height')

plt.show()