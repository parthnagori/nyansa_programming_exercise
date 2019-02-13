import datetime
from heapq import heappush, heappop, heapify
from collections import defaultdict

#TC - O(d), SC - O(d) | d: unique dates
def bucket_sort_dates(dates):
  min_date, max_date = min(dates), max(dates)
  bucket = [[] for i in range((max_date - min_date).days+1)]
  for date in dates:
    bucket[(date - min_date).days].append(date)

  result = []
  for date_vals in bucket:
    result+=date_vals
  return result

#TC - O(unlogun), SC - O(un) | u: unique hit counts | n: unique urls
def heapsort_urlcount(urlcounts):
  q = []
  for url, count in urlcounts.items():
    heappush(q, (-count,url))     
  return q

def get_url_hit_summary(filepath):
  history = defaultdict(dict)
  with open(filepath) as f:
      for line in f:
        date, url = [val.strip() for val in line.split("|")]
        date = datetime.datetime.fromtimestamp(int(date)).date()
        if url in history[date]:
          history[date][url]+=1
        else:
          history[date][url] = 1
  return history

#Time Complexity - O(dunlogun) | Space Complexity - O(dun)
#Assumption: unique dates and uniuqe hit counts are very small
#Time Complexity - O(nlogn) and Space Complexity - O(n)
if __name__=='__main__':
  try:
    filepath = input('Enter file path: ')
    history = get_url_hit_summary(filepath)
    if history:
      sorted_dates = bucket_sort_dates(history.keys())
      for date in sorted_dates:
        print(date.strftime('%m/%d/%Y GMT'))
        q = heapsort_urlcount(history[date])
        while q:
          url = heappop(q)
          print("{} {}".format(url[1], -url[0]))
    else:
      print("Input file is empty")
  except:
    print("File not found at "+filepath)

  

