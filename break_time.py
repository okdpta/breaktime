import webbrowser
import time

total_break = 3
break_count = 0

while(break_count < total_break):

    time.sleep(60*60)
    webbrowser.open('https://www.youtube.com/watch?v=V2-aRHd0kLw')
    break_count = break_count + 1