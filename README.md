# Squareroot 

 - Gönderilen sayının karekökünü hesaplayan API endpoint'tir.
    - Adres: /calculate
    - Adres bir sonuç döndürmez.
 - Karekök, math gibi hazır bir modül kullanılmadan hesaplanır. 
 - Karekök işlemi, asenkron olarak Celery ile yapılır ve veritabanına sonuç bu Celery task'i ile kaydedilir.
 - İşlemin sonucu için:
   - Adres: /results (JSON formatında)
 - Django kullanılmıştır.

  
