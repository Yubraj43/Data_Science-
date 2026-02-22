import bs4
import threading
import requests

urls = (
    'https://www.google.com',
    'https://www.facebook.com',
    'https://www.twitter.com',
    'https://www.linkedin.com',
    'https://www.instagram.com',
    'https://www.youtube.com',
    'https://www.reddit.com',
    'https://www.pinterest.com',
    'https://www.tumblr.com',
    'https://www.flickr.com',
    'https://www.vimeo.com',
    'https://www.wordpress.com',
)

def webscrapping(url):
    res = requests.get(url, timeout=10)
    res.raise_for_status()
    bs4.BeautifulSoup(res.text, 'html.parser')
    print(f"finished scrapping {url}", flush=True)


if __name__ == "__main__":
    threads = []
    for url in urls:
        t = threading.Thread(target=webscrapping, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
        

