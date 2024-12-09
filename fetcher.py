from scrapling.defaults import Fetcher, StealthyFetcher, PlayWrightFetcher

# Fetch websites' source under the radar!
page = StealthyFetcher.fetch('https://www.google.com', headless=True, network_idle=True)
print(page.status)
200
products = page.css('.product', auto_save=True)  # Scrape data that survives website design changes!
print(products)
# Later, if the website structure changes, pass `auto_match=True`
products = page.css('.product', auto_match=True)  # and Scrapling still finds them!
print(products)