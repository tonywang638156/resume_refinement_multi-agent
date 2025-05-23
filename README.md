# 🛒 AutoShopper: Memory-Driven Amazon Shopping Bot

## 📌 Project Description

**AutoShopper** is a fully autonomous AI shopping agent that can purchase products from Amazon on behalf of the user. It leverages memory to learn and remember user preferences (e.g., brand, price range, shipping speed), dynamically compares product options, and interacts with the Amazon website in real-time to **find, evaluate, and purchase** the most suitable item — **without human intervention**.

## 👇 Key Capabilities

- **🧠 User Memory**  
  Stores user preferences such as preferred brands, maximum budget, shipping options, etc.  
  Example: "Prefers Apple over Samsung", "Budget under $200", "Prime shipping only".

- **🕵️ Autonomous Browsing**  
  Uses Playwright or Selenium to navigate Amazon, search for items, and collect product data.

- **📊 Product Comparison**  
  Scrapes and compares listings based on:
  - Price
  - Rating
  - Delivery time
  - Brand
  - Amazon’s Choice or Best Seller tags

- **✅ Best Fit Selection**  
  Applies a weighted scoring system to choose the product that best fits the user's preferences.

- **🛍️ Checkout Automation**  
  Proceeds to checkout (in test mode) by simulating user actions such as:
  - Adding product to cart
  - Navigating to payment
  - Completing the purchase (simulated/demo only)

---

## 🗓️ Week 1 Progress

### ✅ Completed Tasks
- Finalized the use case and project scope.
- Defined the core features and architecture of the system.
- Researched:
  - Amazon's dynamic DOM structure and anti-bot defenses
  - Feasibility of using Playwright/Selenium for Amazon interactions
  - Secure handling of login, sessions, and payment simulation
- Explored strategies for persistent memory using JSON or local database.

### ⚠️ Challenges Identified
- CAPTCHA protection and anti-bot detection mechanisms.
- Handling login and payment securely in a test/demo environment.
- Simulating human-like delays and behavior to avoid being blocked.
