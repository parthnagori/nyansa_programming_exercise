import datetime
from heapq import heappush, heappop, heapify
from collections import defaultdict, OrderedDict

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

#TC - O(unlogn), SC - O(un) | u: unique hit counts | n: unique urls
def heap_sort_urlcount(urlcounts):
  sorted_counts = sorted(set(urlcounts.values()), reverse=True)
  #Ordered Dictionary to store a queue for every unique hit count in descending order
  count_dict = OrderedDict()
  for count in sorted_counts:
    count_dict[count] = []

  #heappush to push urls in sorted order
  for url, count in urlcounts.items():
    heappush(count_dict[count], url)     
  
  return count_dict

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
        count_dict = heap_sort_urlcount(history[date])
        print(date.strftime('%m/%d/%Y GMT'))
        for count, url_q in count_dict.items():
          while url_q:
            url = heappop(url_q)
            print("{} {}".format(url, count))
    else:
      print("Input file is empty")
  except Exception as e:
    print("Following exception occured: {}".format(e))

  

