import webbrowser
import time
url = ["https://www.youtube.com/watch?v=OPf0YbXqDm0","https://www.youtube.com/watch?v=QcIy9NiNbmo","https://www.youtube.com/watch?v=450p7goxZqg","https://www.youtube.com/watch?v=eNxO9MpQ2vA","https://www.youtube.com/watch?v=hT_nvWreIhg"]
total_breaks = 10;
for i in range(total_breaks):
    time.sleep(10)
    webbrowser.open_new(url[i%5])