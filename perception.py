from playwright.sync_api import Page

class Perception:
    def __init__(self, page: Page):
        self.page = page

    def get_products(self):
        results = self.page.query_selector_all("div.s-result-item[data-component-type='s-search-result']")
        products = []
        for item in results:
            title = item.query_selector("h2 a span").inner_text()
            price_tag = item.query_selector("span.a-price-whole")
            price = int(price_tag.inner_text().replace(',', '')) if price_tag else None
            products.append({"title": title, "price": price, "element": item})
        return products
