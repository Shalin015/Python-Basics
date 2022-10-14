import numpy as np
import matplotlib.pyplot as plt

unemployment_Rate = np.array([5.2,5.3,4.3,4.2,4.4,5.1])
Index_Price=np.array([1245,1500,1300,1220,1200,1400])

plt.scatter(unemployment_Rate, Index_Price, color="blue")
plt.title("Unemployment Rate vs Index Price", fontsize=15)
plt.xlabel("Unemployment rate", fontsize="12")
plt.ylabel("Index Rate", fontsize="12")
plt.grid(True)
plt.show()
