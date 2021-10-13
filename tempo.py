segundos_str = input('Digite a quantidade de segundos para converter: ')
total_seg = int(segundos_str)
horas = total_seg // 3600
segs_restantes = total_seg % 3600
minutos = segs_restantes //60
segs_restantes_final = segs_restantes %60
dias = int(horas) // 24
horas_finais = dias % 24
meses = dias // 30
dias_finais = dias % 30
anos = meses // 12
meses_finais = meses %12


print(anos, 'anos, ', meses_finais, 'meses,', dias_finais, 'dias, ', horas_finais, 'horas, ', minutos, 'minutos e',segs_restantes_final, 'segundos')
