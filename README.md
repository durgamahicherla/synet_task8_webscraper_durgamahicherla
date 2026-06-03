# 🕷️ Web Scraper

A Python web scraper that extracts quotes from the web and saves them to CSV.

## 📌 Project Info
- **Internship:** Synent Technologies – Python Development
- **Task:** Task 8 – Web Scraper (Advanced Level)

## 🚀 How to Run

**Step 1:** Install required libraries
```bash
pip install requests beautifulsoup4
```

**Step 2:** Run the scraper
```bash
python web_scraper.py
```

## 🎯 Features
- 🌐 Scrapes quotes from quotes.toscrape.com
- 📄 Multiple pages support
- 💾 Saves data to CSV (output.csv)
- 📊 Shows scraping stats
- ✅ Error handling (no internet, timeout)
- 🏷️ Extracts: Quote, Author, Tags, Page number

## 🛠️ Tech Used
- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `csv` module (built-in)

## 📁 Files
| File | Description |
|------|-------------|
| `web_scraper.py` | Main scraper program |
| `output.csv` | Auto-created scraped data |

## 📸 Sample Output
```
==================================================
   🕷️  Web Scraper - Quotes Scraper
==================================================
🌐 Scraping from: http://quotes.toscrape.com
📄 Pages to scrape: 3

⏳ Scraping page 1... ✅ 10 quotes found!
⏳ Scraping page 2... ✅ 10 quotes found!
⏳ Scraping page 3... ✅ 10 quotes found!

📈 Scraping Summary
Total Quotes Scraped : 30
Unique Authors       : 21
Output File          : output.csv
```

## 👤 Author
Mahicherla Durga Posi Lakshmi– Synent Technologies Internship
