from numpy import *
from pandas import *
from matplotlib.pyplot import *
import xlrd
import openpyxl
from math import *
#zad2 grupa B
x = arange(-100, 100, 0.1)
plot(x, (-4)*x**2+(6*x/2)+20, 'ro', label='(-4)*x**2+(6*x/2)+20')
axis([-2, 4, -25, 25])
legend(loc='lower center')
title('Pierwszy wykres')
show()


plot(x, np.tan(x)-5, label='f(x) = 1/x')
xlabel('x')
ylabel('f(x)')
axis([-2, 6, -40, 80])
legend(loc='lower left')
title('Drugi wykres')
show()

x = arange(-100, 100, 0.1)
plot(x, (-4)*x**2+(6*x/2)+20, 'ro')
plot(x, np.tan(x)-5, label='f(x) = 1/x')
axis([-2, 6, -100, 100])
title('Trzeci wykres')
legend(loc='upper left')
show()