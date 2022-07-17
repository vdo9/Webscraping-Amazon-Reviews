from requests_html import HTMLSession

class Reviews:
    def __init__(self, asin) -> None:
        self.asin = asin
        self.session = HTMLSession()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
        self.url = f'https://www.amazon.com/Superfood-Science-Natural-Organic-Certified/product-reviews/B082XKNFP2/ref=cm_cr_arp_d_viewopt_srt?ie=UTF8&reviewerType=all_reviews&pageNumber=1&sortBy=recent'

    def pagination(self, page):
        r = self.session.get(self.url + str(page))
        if not r.html.find('div[data-hook=review]'):
            return False
        else:
            return r.html.find('div[data-hook=review]')
    
    def parse(self, reviews):
        total = []
        for review in reviews:
            title = review.find('a[data-hook=review-title]', first=True).text, 
            rating = review.find('i[data-hook=review-star-rating] span', first=True).text,
            body = review.find('span[data-hook=review-body] span', first=True).text.replace('\n', '').strip()

            data = {
                'title': title,
                'rating': rating,
                'body': body #did not include [:100] to get amt
            }
            total.append(data)
        return total
    

