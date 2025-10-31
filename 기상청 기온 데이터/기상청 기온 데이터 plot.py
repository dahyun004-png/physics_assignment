import numpy as np
import matplotlib.pyplot as plt

file_path = r"C:\Users\고다현\Documents\이화여대 3학년 2학기\전산물리학\기상청 기온 데이터\OBS_ASOS_DD_20251001143930.csv"

# 예: 3번째 열이 기온 데이터
temp = np.genfromtxt(file_path, delimiter=",", skip_header=1, usecols=3, encoding='cp949')

# x축: 1일부터 데이터 개수만큼 (1, 2, 3, ...)
days = np.arange(1, len(temp) + 1)

plt.figure(figsize=(10,5))
plt.plot(days, temp, marker='s', markeredgecolor='r', markerfacecolor='pink', label='Temperature')

plt.grid(True, linestyle='--', alpha=0.4)
plt.legend(loc='upper right')
plt.xlabel("Time (day)")
plt.ylabel("Temperature (°C)")
plt.title("Average Temperature Data in Seoul.September (Daily Temperature Variation)", 
          fontsize=14, fontweight='bold')

# x축 눈금: 모든 날짜 표시
plt.xticks(days)

plt.tight_layout()
plt.show()
