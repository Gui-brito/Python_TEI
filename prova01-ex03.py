from datetime import date
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
print("Data atual", date.today())
print("Ano atual", date.today().strftime('%Y'))
print("Mês atual", date.today().strftime('%m'))
print("Dia atual", date.today().strftime('%d'))
print("Data atual formatada", date.today().strftime('%d/%m/%Y'))
print("Data formatada por extenso", date.today().strftime('%d de %B de %Y'))