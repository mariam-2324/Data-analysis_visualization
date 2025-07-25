import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

new_stock = pd.read_csv(r'C:\Users\DELL\Documents\GOOGLE-stock.csv')
new_stock.head(30)

dataset1 = (new_stock['High'])
dataset2 = (new_stock['Low'])

plt.plot(dataset1, label='High', color='red', marker='X', linestyle='dotted', markersize=3)
plt.plot(dataset2, label='Low', color='blue', marker='s', linestyle='-', markersize=3)
plt.title('Google Stock Price', fontsize=20, color='green', fontweight='bold', fontstyle='italic', fontfamily='serif')
plt.xlabel('High', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.ylabel('Low', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()





plt.scatter(dataset1, dataset2, label='High', color='red', marker='o')
plt.scatter(dataset1, dataset2, label='Low', color='blue', marker='*')
plt.title('Google Stock Price', fontsize=20, color='green', fontweight='bold', fontstyle='italic', fontfamily='serif')
plt.xlabel('High', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.ylabel('Low', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()


plt.bar(dataset1, dataset2, label='High', color='red', edgecolor='red')
plt.bar(dataset1, dataset2, label='Low', color='blue', edgecolor='red')
plt.title('Google Stock Price', fontsize=20, color='green', fontweight='bold', fontstyle='italic', fontfamily='serif')
plt.xlabel('High', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.ylabel('Low', color='brown', fontsize=15, labelpad=5, fontweight='bold', fontstyle='italic')
plt.legend(loc='upper left')
plt.grid(True)
plt.show()
#SAVE FIGURE
plt.savefig('Google_stock.png', dpi=300, facecolor='orange', edgecolor='black', bbox_inches='tight', pad_inches=0.5)