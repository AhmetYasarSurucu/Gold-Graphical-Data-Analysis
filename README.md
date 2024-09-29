ALTIN GRAFİKSEL VERİ ANALİZİ
 
1.	VERİ KÜMESİNİN AÇIKLAMASI:
Veriler (02/01/2015) - (27/03/2024) tarihleri arasındaki altın kapanış fiyatlarını içermektedir.

1.1 VERİ KAYNAĞI:
Yohoo! Finance’ den veriler çekilmiştir. ( https://finance.yahoo.com/quote/GC=F/ )
 
1.2 VERİ GRAFİĞİ:

 ![image](https://github.com/user-attachments/assets/c01651fe-7252-4d7c-807d-a6831227c37e)
(Gold_chart.py)

2.	DİSTRİBUTİON BOX PLOT:

Dağılım kutu grafiği, bir veri setinin dağılımını görselleştirmek için kullanılan bir grafik türüdür. Bu grafik, veri setinin merkezi eğilimini, dağılımını ve aykırı değerlerini kolayca gösterir.
•	Karşılaştırmalar: Farklı kategoriler arasındaki veri dağılımlarını karşılaştırmak için kullanılabilir. 
o	Örneğin, bir şirketin farklı departmanlarında çalışanların maaşlarını karşılaştırmak için kullanılabilir. 


•	Zaman İçinde Değişim: Zaman serilerindeki veri dağılımını görselleştirmek için de kullanılabilir. 

o	Örneğin, bir hisse senedinin fiyatının bir yıl içindeki dağılımını göstermek için kullanılabilir.

 
•	Veri Aykırılıklarını Belirleme: Dağılım kutu grafiği, veri setindeki aykırı değerleri kolayca tanımlamanıza olanak tanır. 

o	Örneğin, bir sınıftaki öğrencilerin sınav notlarını görselleştirmek ve aykırı öğrencileri belirlemek için kullanılabilir. 


•	Dağılımın Simetrisini ve Merkezi Eğilimi Gösterme: Kutu grafiği, veri setinin simetrisini ve merkezi eğilimini görsel olarak gösterir. Bu, veri setinin genel özelliklerini anlamak için faydalıdır. 


•	İstatistiksel Analizlerde Kullanım: Kutu grafiği, istatistiksel analizlerin bir parçası olarak kullanılabilir. 

o	Örneğin, çeyrekler arası aralık, medyan ve veri setinin dağılımının görsel olarak incelenmesi için kullanılabilir.





2.1	BOX PLOT GRAFİĞİ:
![image](https://github.com/user-attachments/assets/ebf4aabb-7540-4981-85d3-e8cdac81a92c)
(Box_plot_chart.py)

2.2	YORUMU:

•	Q1 (25. Yüzdelik): Bu değer, altın fiyatlarının %25’inin bu değerden (1253.80) düşük olduğunu gösterir. Diğer bir deyişle, altın fiyatlarının çeyreği 1253.80’den daha düşük bir değere sahiptir. 

•	Medyan: Medyan değeri (1462.45), altın fiyatlarının orta noktasını temsil eder. Yani, tüm altın fiyatları sıralandığında, medyan değer ortada yer alır. Bu, genel eğilimi yansıtır ve altın fiyatlarının çoğunluğunun bu değer etrafında toplandığını gösterir. 


•	Ortalama: Ortalama değer (1530.26), tüm altın fiyatlarının toplamının altın fiyatı sayısına bölünmesiyle elde edilir. Bu değer, altın fiyatlarının genel eğilimini yansıtır ve genellikle medyanla birlikte değerlendirilir. 

o	Altın fiyatlarına bakarsak, ortalama değer (1530.26) altın fiyatlarının genel eğilimini yansıtır. Ancak, bu değer, altın fiyatlarının çok yüksek veya çok düşük olduğu dönemlerden büyük ölçüde etkilenebilir. Diğer yandan, medyan değer (1462.45) altın fiyatlarının orta noktasını temsil eder ve aykırı değerlerden etkilenmez.

•	Q3 (75. Yüzdelik): Bu değer (1821.50), altın fiyatlarının %75’inin bu değerden düşük olduğunu gösterir. Diğer bir deyişle, altın fiyatlarının çoğunluğu (yüzde 75) 1821.50’den daha düşük bir değere sahiptir. 

3.	YILLAR ARASI BOX PLOT GRAFİĞİ:
 ![image](https://github.com/user-attachments/assets/8b16c402-edd6-4fac-9fd8-efbaa4394110)
(Yillar_arasi_.py)

3.1	YORUM:
•	2015-2017 Gold Fiyatları Box Plot: 
o	Medyan: 1202.90 USD 
o	Ortalama: 1204.09 USD 
o	Birinci Kuartil (Q1): 1144.03 USD 
o	Üçüncü Kuartil (Q3): 1264.35 USD 
	Grafik, 2015-2017 yılları arasında altın fiyatlarının genellikle 1144.03 USD ile 1264.35 USD arasında değiştiğini gösteriyor. 

•	2017-2019 Gold Fiyatları Box Plot: 
o	Medyan: 1260.70 USD 
o	Ortalama: 1262.64 USD 
o	Birinci Kuartil (Q1): 1225.30 USD 
o	Üçüncü Kuartil (Q3): 1295.80 USD 
	Bu grafik, 2017-2019 yılları arasında altın fiyatlarının bir önceki döneme göre biraz daha yüksek olduğunu gösteriyor. 



•	2019-2021 Gold Fiyatları Box Plot: 
o	Medyan: 1526.50 USD 
o	Ortalama: 1538.32 USD 
o	Birinci Kuartil (Q1): 1409.20 USD 
o	Üçüncü Kuartil (Q3): 1781.90 USD 
	2019-2021 yılları arasında altın fiyatlarında önemli bir artış görülmekte, özellikle üçüncü kuartil değeri oldukça yüksek. 

•	2021-2023 Gold Fiyatları Box Plot: 
o	Medyan: 1795.90 USD 
o	Ortalama: 1789.87 USD 
o	Birinci Kuartil (Q1): 1754.60 USD 
o	Üçüncü Kuartil (Q3): 1841.00 USD 
	Bu dönemde altın fiyatları daha da stabil bir artış göstermiş. 

•	2023-2024 Gold Fiyatları Box Plot: 
o	Medyan: 1944.60 USD 
o	Ortalama: 1942.96 USD 
o	Birinci Kuartil (Q1): 1921.00 USD 
o	Üçüncü Kuartil (Q3): 1983.65 USD 
	En son grafik, altın fiyatlarının son dönemde rekor seviyelere ulaştığını gösteriyor.

4.	YATIRIM ANALİZİ:

4.1    2015-2017 DÖNEMİ: 
Altın fiyatları nispeten düşük ve stabil. Yorum: Bu dönemde, küresel ekonomik büyümenin stabil olduğu ve büyük ekonomik krizlerin yaşanmadığı bir zaman dilimi. Yatırımcılar için altın, düşük riskli bir koruma aracı olarak görülebilir. Tavsiye: Düşük volatilite ve stabil fiyatlar, uzun vadeli yatırımcılar için iyi bir alım fırsatı sunabilir.
 
4.2    2017-2019 DÖNEMİ: 
Fiyatlar bir önceki döneme göre artış göstermiş. Yorum: Bu dönemde, ABD ve Çin arasındaki ticaret savaşları başlamıştır. Belirsizlikler ve riskler arttıkça, yatırımcılar güvenli liman olarak altına yönelmiş olabilir. Tavsiye: Altın, belirsizlik dönemlerinde güvenli bir yatırım aracı olarak değerlendirilebilir. Yatırımcılar, portföylerini çeşitlendirerek risklerini yönetebilir. 
 
4.3    2019-2021 DÖNEMİ: 
Altın fiyatlarında önemli bir artış ve volatilite görülüyor. Yorum: COVID-19 pandemisi küresel ekonomiyi sarsmış ve büyük ekonomik belirsizliklere yol açmıştır. Bu dönemde altın fiyatları rekor seviyelere ulaşmıştır. Tavsiye: Kriz dönemlerinde altın, değerini koruma konusunda güçlü bir araç olarak öne çıkar. Yatırımcılar, likidite ihtiyaçlarını göz önünde bulundurarak yatırımlarını planlamalıdır. 
 
4.4	2021-2023 DÖNEMİ: 
Fiyatlar stabil bir artış trendi gösteriyor. Yorum: Pandemi sonrası toparlanma süreci ve ekonomik teşvik paketleri, piyasalarda bir miktar stabilizasyon sağlamış olabilir. Ancak, enflasyon endişeleri altın fiyatlarını yukarı yönlü baskılamış olabilir. Tavsiye: Enflasyon karşısında korunma amacıyla altın, portföylerde önemli bir yer tutmaya devam eder. Yatırımcılar, enflasyonist baskıları göz önünde bulundurarak hareket etmelidir.
 
4.5    2023-2024 DÖNEMİ: 
Altın fiyatları rekor seviyelere ulaşmış. Yorum: Küresel ekonomik belirsizliklerin devam etmesi, altın fiyatlarını yükseltmiş olabilir. Ayrıca, merkez bankalarının politikaları ve döviz kurlarındaki dalgalanmalar da etkili olmuştur. Tavsiye: Yatırımcılar, piyasa koşullarını yakından takip ederek, altın yatırımlarını zamanlamalı ve risk yönetimini etkin bir şekilde yapmalıdır.


5.	GENEL YORUM:
Eğer kısa dönem hareketli ortalamalar, uzun dönem hareketli ortalamaların üzerine çıkarsa, bu bir yükseliş trendinin başlangıcı olarak yorumlanabilir. Bu durumda, 2024-2026 yılları arasında fiyatların yükselmesi öngörülebilir.
