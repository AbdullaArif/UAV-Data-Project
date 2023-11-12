import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time

# Excel tablosu oluşturun ve verileri doldurun
sensor_data = pd.DataFrame({
    'Zaman': np.arange(0, 100, 1),  # Zamanı temsil eden bir sütun
    'Yükseklik': np.random.uniform(0, 100, 100),  # Rastgele yükseklik verisi
    'Hız': np.random.uniform(0, 50, 100)  # Rastgele hız verisi
})

# Kullanıcıdan alınan frekans
frekans = int(input("Verilerin kaç saniyede bir gösterilmesini istersiniz? "))

# Verileri ekranda gösteren kod
while True:
    for index, row in sensor_data.iterrows():
        print(f"Zaman: {row['Zaman']} saniye, Yükseklik: {row['Yükseklik']}, Hız: {row['Hız']}")
        time.sleep(1 / frekans)  # Kullanıcının belirlediği frekansta bekletme
        # Ekran temizleme işlemi (Windows için)
        _ = os.system('cls' if os.name == 'nt' else 'clear')

    devam_et = input("Devam etmek istiyor musunuz? (E/H): ")
    if devam_et.upper() != 'E':
        break
