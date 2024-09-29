import yfinance as yf  # yfinance kütüphanesini yf kısaltmasıyla içe aktarıyoruz.
import pandas as pd  # pandas kütüphanesini pd kısaltmasıyla içe aktarıyoruz.

def get_Gold_price():
    Gold_ticker = "GC=F"  # Altın Yahoo Finance'teki sembolü
    Gold_data = yf.download(Gold_ticker, start="2015-01-01")  # 2020-01-01 tarihinden itibaren altın verilerini indiriyoruz.
    if not Gold_data.empty:  # Veri boş değilse devam ediyoruz
        return Gold_data["Close"]  # Altın verilerinin kapanış fiyatlarını döndürüyoruz.
    return None  # Veri boşsa None döndürüyoruz.

Gold_prices = get_Gold_price()                                     # Altın fiyatlarını alıyoruz.
if Gold_prices is not None and not Gold_prices.empty:              # Altın fiyatı varsa ve boş değilse
    Gold_prices_df = pd.DataFrame(Gold_prices, columns=["Close"])  # Pandas DataFrame oluşturuyoruz, sütun adını "Close" olarak belirtiyoruz
    Gold_prices_df.to_excel("Gold.xlsx", index=True)    # Verileri Excel dosyasına yazıyoruz, index=True indeksleri de dahil eder
    print("Veriler başarıyla Excel dosyasına aktarıldı.")          # Başarılı bir mesaj yazdırıyoruz.
else:
    print("Altın fiyatları bulunamadı.")
