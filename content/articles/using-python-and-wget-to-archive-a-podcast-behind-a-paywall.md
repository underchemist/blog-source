Title: Using python and wget to download the entire comedy bang bang archive to-date
Tags: python, comedy
Date: 2018-01-10 18:09
Modified: 2018-01-10 22:55
Summary: Use a free Howl premium trial to find find the download links for all the comedy bang bang podcast episodes, wget to download them.
Status: published

I love [Comedy Bang Bang!](http://www.earwolf.com/show/comedy-bang-bang/) so much, it's gotten me through some unhappy times.  Unfortunately all but
the past 6 months or so of episodes are archived behind a paywall. Supporting Earwolf and the
comedians that provide literally countless hours of free content is something I am in fact very
much in support of. But one day there is the chance I want to revisit a very old episode but the
hosting service has shutdown or just life has happened and there isn't a reliable way of accessing
all the old archives anymore.

So I did slightly unethical thing. I signed up for a free trial of howl premium (which I've had
before) and went to the Howl archive url and did little digging with chrome dev tools. Initially I
had assumed I would be able to right click the rendered episodes and find the mp3 url from there,
but they had hid it away a little bit. From the source I was able to find the episode-table id
whose elements contained a tags with a data-stream-url attribute. These data-stream-url links
were to s3.aws servers and had the mp3 filename directly in the url! Some quick curl on a few
different of these urls proved that they were indeed the podcast audio files.

To quickly scrape all these urls I used [BeautifulSoup](https://pypi.python.org/pypi/beautifulsoup4) on the source file I saved.

```python
from bs4 import BeautifulSoup

f = open('Comedy Bang Bang_ The Podcast - Howl.html', 'r')
soup = BeautifulSoup(f, 'html.parser')
links = soup.find_all('a')
a = []
for link in links:
     a.append(link.get('data-stream-url'))

# a also contains many None entries for all a tags without data-stream-url attribute
b = []
for i in a:
     if i:
          b.append(i)

with open('cbb-archive-urls.txt', 'w') as f:
     for i in b:
          f.write(i + '\n')
```

It turns out wget is quite feature rich and can be [configured quite a bit](https://www.gnu.org/software/wget/manual/wget.html). wget handles an input file of urls sequentially, with the additional arguments helping to make sure the queue can be resumed, doesn't abuse their hosting server too much, and doesn't eat up all my bandwidth.

```bash
wget --limit-rate=1000k -c -t 10 --wait 12 --random-wait -i /mnt/c/Users/ysebastien/Downloads/cbb-archive-urls.txt
```