# Pager (IOT Project)
A pager device that uses wifi to communicate with server connected in the same network. A pager device consists of an ESP32, Buzzer, LED, (128x64)OLED screen, battery and two buttons.

The message is sent from the server to all the pager devices using UDP protocol. The pager devices can either send a yes or no by pressing the respective buttons.

Pager Device Blueprint (without the OLED connection):
![pager_diag](https://user-images.githubusercontent.com/73333888/221413632-6421c411-5cfc-4ef8-9eb2-f39dc628fa48.png)

Pager Device setup:
![pager](https://user-images.githubusercontent.com/73333888/221413647-ee68529d-ca3b-41ed-a8ba-7e1bf8907687.jpg)



