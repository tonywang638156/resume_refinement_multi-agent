# session_manager.py

import json
import os
from cryptography.fernet import Fernet
from playwright.async_api import async_playwright

SESSION_FILE = "session_data.json"
KEY_FILE = "session_key.key"

def generate_key():
    """
    Generates a key for encrypting session data.
    """
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)

def load_key():
    """
    Loads the encryption key.
    """
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def save_encrypted_session(data):
    """
    Encrypts and saves session cookies to a JSON file.
    """
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(json.dumps(data).encode())
    with open(SESSION_FILE, "wb") as f:
        f.write(encrypted_data)

def load_encrypted_session():
    """
    Loads and decrypts session cookies from the JSON file.
    """
    if not os.path.exists(SESSION_FILE):
        return None
    key = load_key()
    fernet = Fernet(key)
    with open(SESSION_FILE, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return json.loads(decrypted_data)

async def create_browser_context(playwright):
    """
    Creates a persistent browser context using session data.
    """
    session_data = load_encrypted_session()
    context = await playwright.chromium.launch_persistent_context(
        user_data_dir="./user_data",
        headless=False
    )
    if session_data:
        await context.add_cookies(session_data)
    return context

async def save_session_cookies(context):
    """
    Saves the session cookies after scraping completes.
    """
    cookies = await context.cookies()
    save_encrypted_session(cookies)
