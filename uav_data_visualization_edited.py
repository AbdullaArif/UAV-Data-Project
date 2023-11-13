import cv2
import pandas as pd

#Excel dosyasındakı Rastgele bilgileri table değerine pandası kullanarak veriyoruz.
table = pd.read_excel('DATA.xlsx', 'FakeData')

#Alınmış bilgileri Excel taplosuna uygun olarak tolist() metodu ile liste haline getiriyoruz.
roll = table['ROLL'].tolist()
yaw = table['YAW'].tolist()
pitch = table['PITCH'].tolist()
lvl = table['LVL'].tolist()
bat_percentage = table['CHRG'].tolist()
airspeed = table['AS'].tolist()
ground_speed = table['GS'].tolist()
signal = table['LVL'].tolist()
mode = table['MODE'].tolist()
temp = table['TEMP'].tolist()
altitude = table['ALT'].tolist()
vertical_speed = table['ROC'].tolist()
bat_voltage = table['V'].tolist()
bat_current = table['A'].tolist()
x = table['X'].tolist()
y = table['Y'].tolist()

i = 0
while True:

    img = cv2.imread('arazi1.jpg')


    cv2.putText(img, f'ALT:{altitude[i]:.2f}m', (550, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (255, 0, 0), 1)
    cv2.putText(img, f'GPS:{x[i]:.2f}; {y[i]:.2f}', (500, 370), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                (0, 0, 255), 1)
    cv2.putText(img, f'{mode[i]}', (69, 80), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                (255, 0, 0), 1)
    cv2.putText(img, f'TAT:{temp[i]}C', (590, 80), cv2.FONT_HERSHEY_COMPLEX, 0.6,
                (255, 0, 0), 1)
    cv2.putText(img, f'ROC:{vertical_speed[i]:.2f}m/s', (550, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (255, 0, 0), 1)
    cv2.putText(img, f'AS:{airspeed[i]:.2f}m/s', (20, 30), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (255, 0, 0), 1)
    cv2.putText(img, f'GS:{ground_speed[i]:.2f}m/s', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.5,
                (255, 0, 0), 1)
    cv2.putText(img, f'BAT:{bat_percentage[i]:.0f}% {bat_voltage[i]:.0f}V {bat_current[i]:.0f}A', (20, 370),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(img, f'ROLL:{roll[i]:.0f} YAW:{yaw[i]:.0f} PITCH:{pitch[i]:.0f}', (190, 30),
                cv2.FONT_HERSHEY_COMPLEX, 0.6, (250, 84, 36), 1)


    if roll[i] > 60 or roll[i] < -60:
        cv2.putText(img, f'BANK ANGLE', (240, 130), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (0, 0, 255), 2)

    if pitch[i] > 15:
        cv2.putText(img, f'STALL', (290, 100), cv2.FONT_HERSHEY_COMPLEX, 1,
                    (0, 0, 255), 2)

    if bat_percentage[i] < 25:
        cv2.putText(img, f'LOW BATTERY', (130, 300), cv2.FONT_HERSHEY_COMPLEX, 2,
                    (0, 0, 255), 3)

    i += 1
    if i >= len(airspeed) - 1:
        i = 0

    cv2.imshow('FPV', img)

    if cv2.waitKey(1000) == 27:
        break

