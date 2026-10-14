from datetime import  datetime

current_time = datetime.now().time()
formatted_time = current_time.strftime("%I:%M %p")
print(formatted_time)