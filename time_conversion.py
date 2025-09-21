from datetime import datetime
s='12:40:22AM'
_time=datetime.strptime(s, '%I:%M:%S%p')
print(_time.strftime('%H:%M:%S'))