from schedule import * 
import schedule
import time
 
def job():
    print("Schedule Test")

schedule.every(1).second.do(job)

count = 0

while True:
    schedule.run_pending()
    count += 1
    time.sleep(1)
    print(count)