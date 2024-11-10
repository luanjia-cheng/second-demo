import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.interpolate import interp1d

# 已知数据点
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 1, 4, 9, 16])

# 创建插值函数，'linear' 表示线性插值
f = interp1d(x, y, kind='linear')

# 生成新数据点
x_new = np.linspace(0, 4, 100)
y_new = f(x_new)

# 绘制插值结果
plt.plot(x, y, 'o', label='Known data')
plt.plot(x_new, y_new, '-', label='Interpolated curve')
plt.legend()
plt.show()
