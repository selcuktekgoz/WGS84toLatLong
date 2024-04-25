# WGS84toLatLong
Bu proje Belediyelerin _Kent Otomasyon Sistemi (KEOS)_ yazılımı üzerinden sunduğu hizmetlerdeki WGS84 koordinat sisteminin (Lat. ,Long.) koordinatları olarak çevrilmesi amacıyla oluşturulmuştur.
___

## Kullanım
___
Örnek kullanım senaryosu Niğde Belediyesi KEOS hizmeti üzerinden verilmiştir.

1. `pip install -r requirements.txt` ile gerekli kütüphaneleri kuralım.
 

2. _WGS84_ kordinatlarının elde edilmesi. 
Niğde Belediyesi keos hizmeti üzerinden verilerimizi kazıyalım. [Link](https://keos.nigde.bel.tr/keos/)

[media_1.mp4](media%2Fmedia_1.mp4)
3. Kazıdığımız _WGS84_ kordinatlarını (Lat,Long) çevirmek için proje dizininde bir txt dosyasına kaydedip. Aşağıdaki komutları çalıştıralım.

`file = open_file("ahipasa_mah.txt")`

`df = convert_wgs84_to_lat_long(file,"Niğde")`

[media_2.mp4](media%2Fmedia_2.mp4)


İşlem sonucunda proje dizinimizde _"ahipasa_mah_2024_04_25_15_52_07.csv"_ isminde dosyamız oluşmuştur.

| LATITUDE  | LONGITUDE  |
| --- | --- |
| 37.96694244789013 | 34.67551747005115 |
| 37.96818660709222 | 34.67633071578051 |
| 37.96741328520884 | 34.67842010521701 |
