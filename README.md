# WGS84toLatLong
Bu proje Belediyelerin _Kent Otomasyon Sistemi (KEOS)_ yazılımı üzerinden sunduğu hizmetlerdeki WGS84 koordinat sisteminin (Lat. ,Long.) koordinatları olarak çevrilmesi amacıyla oluşturulmuştur.
___

## Kullanım
___
Örnek kullanım senaryosu Niğde Belediyesi KEOS hizmeti üzerinden verilmiştir.

1. `pip install -r requirements.txt` ile gerekli kütüphaneleri kuralım.
 

2. _WGS84_ kordinatlarının elde edilmesi. 
Niğde Belediyesi keos hizmeti üzerinden verilerimizi kazıyalım. [Link](https://keos.nigde.bel.tr/keos/)



https://github.com/selcuktekgoz/WGS84toLatLong/assets/102700589/6ea52662-3297-4781-b540-5a1b0a9a70dc



3. Kazıdığımız _WGS84_ kordinatlarını (Lat,Long) çevirmek için proje dizininde bir txt dosyasına kaydedip. Aşağıdaki komutları çalıştıralım.

`file = open_file("ahipasa_mah.txt")`

`df = convert_wgs84_to_lat_long(file,"Niğde")`



https://github.com/selcuktekgoz/WGS84toLatLong/assets/102700589/5e52d205-28c9-44b6-bed4-b6fea011fff1




İşlem sonucunda proje dizinimizde _"ahipasa_mah_2024_04_25_15_52_07.csv"_ isminde dosyamız oluşmuştur.

| LATITUDE  | LONGITUDE  |
| --- | --- |
| 37.96694244789013 | 34.67551747005115 |
| 37.96818660709222 | 34.67633071578051 |
| 37.96741328520884 | 34.67842010521701 |
