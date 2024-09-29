import pandas as pd  # Pandas kütüphanesini içe aktarır
import matplotlib.pyplot as plt  # Matplotlib kütüphanesinin pyplot modülünü içe aktarır

# Excel dosyasını oku
veri = pd.read_excel('Gold.xlsx')  # 'Gold.xlsx' dosyasından veriyi okur

# Tarih sütununu indeks olarak ayarla
veri.set_index('Date', inplace=True)  # 'Date' sütununu indeks olarak ayarlar ve veriyi değiştirir (inplace=True)

# Zaman serisi grafiği çiz
plt.figure(figsize=(10, 6))  # Yeni bir çizim alanı oluşturur ve boyutunu belirler
veri['Close'].plot()  # 'Close' sütunundaki veriyi zaman serisi grafiği olarak çizer
plt.title('Gold Fiyatları Zaman Serisi Grafiği')  # Grafiğin başlığını ayarlar
plt.xlabel('Tarih')  # X ekseninin etiketini ayarlar
plt.ylabel('Kapanış Fiyatı')  # Y ekseninin etiketini ayarlar
plt.grid(True)  # Izgara çizgilerini etkinleştirir
plt.show()  # Grafiği görüntüler
