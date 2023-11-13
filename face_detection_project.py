import cv2

# Resim dosyasının adını belirtin
resim_adi = "yuzResmi2.jpg"  # Bu dosya adını, kullanacağınız resim dosyasının adıyla değiştirin

# Cascade Classifier'ı yüz tespiti için yükleyin
yuz_tespiti_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Resmi okuyun
resim = cv2.imread(resim_adi)
# Gri tonlamaya dönüştürün (yüz tespiti için genellikle gri tonlama kullanılır)
gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)

# Yüz tespiti
yuzler = yuz_tespiti_cascades.detectMultiScale(gri_resim, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Tespit edilen yüzleri işaretleyin
for (x, y, w, h) in yuzler:
    cv2.rectangle(resim, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Sonucu göster
cv2.imshow('Yuz Tespiti', resim)
cv2.waitKey(0)
cv2.destroyAllWindows()
