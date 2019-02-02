import datetime
from heapq import heappush, heappop, heapify
from collections import defaultdict

#TC - O(d), SC - O(d) | d: unique dates
def bucket_sort_dates(dates):
  min_date, max_date = min(history.keys()), max(history.keys())
  bucket = [[] for i in range((max_date - min_date).days+1)]
  for date in dates:
    bucket[(date - min_date).days].append(date)

  result = []
  for dates in bucket:
    result+=dates
  return result

#TC - O(unlogn), SC - O(un) | u: unique hit counts | n: unique urls
def bucket_sort_urlcount(urlcounts):
  max_count = max(urlcounts.values())
  bucket = [[] for i in range(max_count+1)]
  for url, count in urlcounts.items():
    heappush(bucket[count], url)     
  
  return bucket

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

#Time Complexity - O(dunlogn) | Space Complexity - O(dun)
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
        sorted_urls = bucket_sort_urlcount(history[date])
        for i in range(len(sorted_urls) - 1, 0, -1):
          for url in sorted_urls[i]:
            print("{} {}".format(url, i))
    else:
      print("Input file is empty")
  except:
    print("File not found at "+filepath)

  

