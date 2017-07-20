import wget
import time
import schedule

def date_():
    return time.strftime("%Y%m%d")
def time_():
    return time.strftime("%H%M")

def job():
    print(time_())
    url="http://weather.tmd.go.th/stp/stp240_latest.gif"
    save_as = "./stp240_" + date_() + time_() + ".gif"
    wget.download(url=url, out=save_as, bar=None)

schedule.every().hours.at("00:00").do(job)
schedule.every().hours.at("00:15").do(job)
schedule.every().hours.at("00:30").do(job)
schedule.every().hours.at("00:45").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
