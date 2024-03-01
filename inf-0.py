import numpy as np
from scipy import stats

price_15_pro_max = [16000.00, 14600.00, 21900.00, 19500.00, 19500.00, 22900.00, 22900.00, 24000.00, 26900.00]
mean_15_pro_max = np.mean(price_15_pro_max)
median_15_pro_max = np.median(price_15_pro_max)
mode_15_pro_max = stats.mode(price_15_pro_max)
print("Apple iPhone 15 Pro Max")
print("Average price: " + str(mean_15_pro_max))
print("Median price: " + str(median_15_pro_max))
print("Modal price: " + str(mode_15_pro_max))
print(" ")

price_15_pro = [14500.00, 14500.00, 16900.00, 16500.00]
mean_15_pro = np.mean(price_15_pro)
median_15_pro = np.median(price_15_pro)
mode_15_pro = stats.mode(price_15_pro)
print("Apple iPhone 15 Pro")
print("Average price: " + str(mean_15_pro))
print("Median price: " + str(median_15_pro))
print("Modal price: " + str(mode_15_pro))