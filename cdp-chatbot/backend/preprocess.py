from bs4 import BeautifulSoup
import requests
import json

def scrape_and_store(url, filename, selectors):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = {}
    for selector, key in selectors.items():
        element = soup.select_one(selector)
        if element:
            data[key] = element.get_text(strip=True)
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

scrape_and_store("https://segment.com/docs", "segment.json", {
    "h1": "setup_new_source"
})
scrape_and_store("https://docs.mparticle.com", "mparticle.json", {
    "h1": "create_user_profile"
})
scrape_and_store("https://docs.lytics.com", "lytics.json", {
    "h1": "build_audience_segment"
})
scrape_and_store("https://docs.zeotap.com", "zeotap.json", {
    "h1": "integrate_data"
})
