import pandas as pd  # Pandas kütüphanesini içe aktarır
import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot modülünü içe aktarır

# Excel dosyasını oku
veri = pd.read_excel('Gold.xlsx')  # 'Gold.xlsx' dosyasından veriyi okur

# Box plot için renk ve özellikler
boxprops = dict(linestyle='-', linewidth=2, color='b', alpha=0.5)  # Kutu çizgilerinin özelliklerini tanımlar
medianprops = dict(linestyle='-', linewidth=2, color='r', alpha=0.5)  # Median çizgisinin özelliklerini tanımlar
meanprops = dict(marker='o', markerfacecolor='green', markersize=8, markeredgecolor='black')  # Ortalama işaretinin özelliklerini tanımlar

# Box plot çiz
plt.figure(figsize=(10, 6))  # Yeni bir çizim alanı oluşturur ve boyutunu belirler
box = plt.boxplot(veri['Close'],  # 'Close' sütunundaki veriyi kullanarak kutu grafiği çizer
                  patch_artist=True,  # Kutuları renklendirir
                  boxprops=boxprops,  # Kutu çizgilerinin özelliklerini belirtir
                  medianprops=medianprops,  # Median çizgisinin özelliklerini belirtir
                  meanprops=meanprops,  # Ortalama işaretinin özelliklerini belirtir
                  showmeans=True,  # Ortalamayı gösterir
                  notch=True)  # Kutuların içinde kesik oluşturur (notch)

# Outlier'ları al
outliers = [flier.get_ydata() for flier in box['fliers']]  # Aykırı değerleri alır

plt.title('Gold Fiyatları Box Plot')  # Grafiğin başlığını ayarlar
plt.ylabel('Kapanış Fiyatı')  # Y ekseninin etiketini ayarlar
plt.grid(True)  # Izgara çizgilerini etkinleştirir

# Açıklamaları ekle
plt.text(1.1, veri['Close'].median(), f'Median: {veri["Close"].median():.2f}', verticalalignment='center', color='r', fontsize=10)  # Median değerini ekle
plt.text(1.1, veri['Close'].mean(), f'Mean: {veri["Close"].mean():.2f}', verticalalignment='center', color='green', fontsize=10)  # Ortalama değerini ekle
plt.text(1.1, veri['Close'].quantile(0.25), f'Q1 (25th percentile): {veri["Close"].quantile(0.25):.2f}', verticalalignment='center', color='b', fontsize=10)  # Q1 değerini ekle
plt.text(1.1, veri['Close'].quantile(0.75), f'Q3 (75th percentile): {veri["Close"].quantile(0.75):.2f}', verticalalignment='center', color='b', fontsize=10)  # Q3 değerini ekle

# Veri noktalarını ekleyerek dağılımı göster
plt.scatter(x=[1] * len(veri), y=veri['Close'], color='orange', alpha=0.3, label='Veri Noktaları')  # Veri noktalarını scatter plot ile çizer

# Outlier'ları scatter plot olarak çiz
for outlier in outliers:  # Her aykırı değer için
    plt.scatter(x=[1] * len(outlier), y=outlier, color='red', alpha=0.3, s=100, label='Outliers')  # Aykırı değerleri scatter plot ile çizer

plt.legend()  # Lejantı gösterir

plt.show()  # Grafiği görüntüler
