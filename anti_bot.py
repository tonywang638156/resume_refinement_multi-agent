# anti_bot.py

import random
import time
from playwright.async_api import Page

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:110.0) Gecko/20100101 Firefox/110.0",
]

def get_random_user_agent():
    return random.choice(USER_AGENTS)

async def apply_human_delay(min_delay=2, max_delay=5):
    delay = random.uniform(min_delay, max_delay)
    await asyncio.sleep(delay)

async def detect_captcha(page: Page):
    """
    Detects if a CAPTCHA is present on the current page.
    For Amazon, look for known CAPTCHA selectors.
    """
    captcha_selectors = [
        "form[action='/errors/validateCaptcha']",
        "img[src*='captcha']",
    ]
    for selector in captcha_selectors:
        if await page.query_selector(selector):
            print("⚠️ CAPTCHA detected! Pausing scraping and requiring manual intervention.")
            return True
    return False
