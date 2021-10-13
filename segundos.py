segundos = int(input('Por favor, entre com o número de segundos que deseja converter:'))
d = segundos % 60
minutos = segundos // 60
c = minutos % 60
horas = minutos // 60
b = horas % 24
a = horas // 24
print(a,'dias,',b,'horas,',c,'minutos e',d,'segundos.')
