import queue
import threading
import time
import urllib.request
import os
from fb_scrapper import scrape_groups_pages
from aws_s3 import init_s3
exitFlag = 0

class scrapeThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
   def run(self):
      print ("Starting " + self.name)
      process_data()
      print ("Exiting " + self.name)

def process_data():
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = workQueue.get()
         queueLock.release()
         full_scrape, use_kafka = get_scrape_type()
         scrape_groups_pages(data, full_scrape, use_kafka, False)
         if "COMMENTS" in os.environ:
             scrape_groups_pages(data, 0, 2, True)
      else:
         queueLock.release()
         time.sleep(1)
def load_id_file(path):
    try:
        lines = open(path).read().splitlines()
    except:
        print("failed to find file now going based on environment variable url")
        #data = urllib.request(os.envi)
        data = os.environ['IDS']
        lines = data.split(",")
    return lines
def start_threads(threadList):
    threads = []
    threadID = 1
    for tName in threadList:
       thread = scrapeThread(threadID, tName)
       thread.start()
       threads.append(thread)
       threadID += 1
    return threads
def init_queue(nameList):
    workQueue = queue.Queue(10)
    queueLock.acquire()
    for word in nameList:
       workQueue.put(word)
    queueLock.release()
    return workQueue
def get_scrape_type():
    # Somewhat backwards but for kafka one is false and 0 is true
    # By default do not use Kafka
    use_kafka = 1
    if "USE_KAFKA" in os.environ:
        use_kafka =0
    # By default only scrape since last time stamp
    full_scrape = 1
    if "FULL_SCRAPE" in os.environ
        if os.environ['FULL_SCRAPE'] is "0":
            full_scrape = 0
    return full_scrape, use_kafka


threadList = ["Thread-1", "Thread-2", "Thread-3"]
nameList = load_id_file("id.txt")
queueLock = threading.Lock()
workQueue = init_queue(nameList)

# Create new threads
threads = start_threads(threadList)

# Wait for queue to empty
while not workQueue.empty():
   pass

# Notify threads it's time to exit
exitFlag = 1

# Wait for all threads to complete
for t in threads:
   t.join()
print ("Exiting Main Thread")
print(os.environ["USE_AWS"])
if os.environ["USE_AWS"] is "1":
    init_s3()
    print("files saved to AWS")
