import pandas as pd
import matplotlib.pyplot as plt

# Excel dosyasını oku
veri = pd.read_excel('Gold.xlsx')

# Yıllara göre veriyi filtrele ve box plotları çiz
years = [(2015, 2017), (2017, 2019), (2019, 2021), (2021, 2023), (2023, 2024)]

for i, (start_year, end_year) in enumerate(years, start=1):
    filtered_data = veri[(veri['Date'].dt.year >= start_year) & (veri['Date'].dt.year < end_year)]

    # Box plot için renk ve özellikler
    boxprops = dict(linestyle='-', linewidth=2, color='b', alpha=0.5)
    medianprops = dict(linestyle='-', linewidth=2, color='r', alpha=0.5)
    meanprops = dict(marker='o', markerfacecolor='green', markersize=8, markeredgecolor='black')

    # Box plot çiz
    plt.figure(figsize=(10, 6))
    box = plt.boxplot(filtered_data['Close'],
                      patch_artist=True,
                      boxprops=boxprops,
                      medianprops=medianprops,
                      meanprops=meanprops,
                      showmeans=True,
                      notch=True)

    outliers = [flier.get_ydata() for flier in box['fliers']]

    plt.title(f'Gold Fiyatları Box Plot ({start_year}-{end_year})')
    plt.ylabel('Kapanış Fiyatı')
    plt.grid(True)

    plt.text(1.1, filtered_data['Close'].median(), f'Median: {filtered_data["Close"].median():.2f}',
             verticalalignment='center', color='r', fontsize=10)
    plt.text(1.1, filtered_data['Close'].mean(), f'Mean: {filtered_data["Close"].mean():.2f}',
             verticalalignment='center', color='green', fontsize=10)
    plt.text(1.1, filtered_data['Close'].quantile(0.25),
             f'Q1 (25th percentile): {filtered_data["Close"].quantile(0.25):.2f}', verticalalignment='center',
             color='b', fontsize=10)
    plt.text(1.1, filtered_data['Close'].quantile(0.75),
             f'Q3 (75th percentile): {filtered_data["Close"].quantile(0.75):.2f}', verticalalignment='center',
             color='b', fontsize=10)

    plt.scatter(x=[1] * len(filtered_data), y=filtered_data['Close'], color='orange', alpha=0.3, label='Veri Noktaları')
    for outlier in outliers:
        plt.scatter(x=[1] * len(outlier), y=outlier, color='red', alpha=0.3, s=100, label='Outliers')

    plt.legend()
    plt.show()
