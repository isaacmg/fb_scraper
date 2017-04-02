import queue
import threading
import time
from get_posts import scrape_comments_from_last_scrape, scrape_posts_from_last_scrape_kafka
exitFlag = 0

class scrapeThread (threading.Thread):
   def __init__(self, threadID, name):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name

   def run(self):
      print ("Starting " + self.name)
      process_data(self.name)
      print ("Exiting " + self.name)

def process_data():
   while not exitFlag:
      queueLock.acquire()
      if not workQueue.empty():
         data = workQueue.get()
         queueLock.release()
         scrape_posts_from_last_scrape_kafka(data)
      else:
         queueLock.release()
         time.sleep(1)
def load_id_file(path):
    lines = open(path).read().splitlines()
    print(lines)
    return lines
def start_threads(threadList):
    threads = []
    threadID = 1
    for tName in threadList:
       thread = scrapeThread(threadID, tName, workQueue)
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
