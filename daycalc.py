from datetime import date
f_date = date(y, m, d)
l_date = date(y, m, d)
delta = l_date - f_date
print(delta.days)
