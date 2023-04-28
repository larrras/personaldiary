from datetime import datetime 

today = datetime.now()

date_time = today.strftime('%d/%m/%Y %H:%M:%S')
print(date_time)