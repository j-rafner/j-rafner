import numpy as np
import matplotlib.pyplot as plt

tid = np.array([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260])  
temp_målt = np.array([88.2, 53.9, 42.5, 37.5, 34.0, 31.5, 28.5, 27.0, 25.6, 24.6, 23.9, 23.2, 23.1, 22.4])  
Tk = 22  


T0 = temp_målt[0]  
log_diff = np.log(temp_målt - Tk)  
a = -(log_diff[-1] - log_diff[0]) / (tid[-1] - tid[0])  


tid_newton = np.linspace(0, 260, 100)
temp_newton = Tk + (T0 - Tk) * np.exp(-a * tid_newton)


plt.plot(tid, temp_målt, '-', label="Ananasen")
plt.plot(tid_newton, temp_newton, '-', label="Newtons avkjølingslov")
print(a)
plt.xlabel("Tid (minutter)")
plt.ylabel("Temperatur (celcius)")
plt.legend()
plt.grid()
plt.title("Ananasen")
plt.show()
