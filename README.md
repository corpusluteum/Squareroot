# Squareroot 

 - Gönderilen sayının karekökünü hesaplayan API endpoint'tir.
    - Adres: /calculate
    - Veri: JSON formatında {'number': 16} şeklinde hesaplanacak sayı
    - Adres bir sonuç döndürmez.
 - İşlem sonucu veritabanına kaydedilir.
 - Karekök, math gibi hazır bir modül kullanmadan hesaplanır. 
 - Karekök işlemi, asenkron olarak Celery ile yapılır ve veritabanına sonuç bu Celery task'i ile yapılır.
 - İşlemin sonucu için:
   - Adres: /results (JSON formatında)

  
