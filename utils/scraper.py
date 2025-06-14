import asyncio
from playwright.async_api import async_playwright
import random

async def scrape_amazon(query, preferences):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.amazon.com/")
        await page.fill("input[name='field-keywords']", query)
        await page.click("input#nav-search-submit-button")

        # Random delay to simulate human browsing
        await asyncio.sleep(random.uniform(2, 5))

        product_cards = await page.query_selector_all("div.s-main-slot div[data-component-type='s-search-result']")
        products = []
        for card in product_cards[:10]:
            title = await card.query_selector_eval("h2 a span", "el => el.innerText")
            price = await card.query_selector_eval("span.a-price span.a-offscreen", "el => el.innerText", force_expr=True) or "N/A"
            rating = await card.query_selector_eval("span.a-icon-alt", "el => el.innerText", force_expr=True) or "N/A"
            badge = await card.query_selector_eval("span.s-label-popover-default", "el => el.innerText", force_expr=True) or ""
            products.append({
                "title": title,
                "price": price,
                "rating": rating,
                "badge": badge
            })

        await browser.close()
        return products

# example usage:
# asyncio.run(scrape_amazon("wireless mouse", {"preferred_brands": ["Logitech"], "max_budget": 50}))
