import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime

# ============================================
# Web Scraper - Scrapes quotes from website
# Website: quotes.toscrape.com (free practice site)
# ============================================

BASE_URL = "http://quotes.toscrape.com"
OUTPUT_FILE = "output.csv"

def scrape_quotes(max_pages=3):
    """Quotes scrape cheyyi multiple pages nundi"""
    
    all_quotes = []
    
    print("=" * 50)
    print("   🕷️  Web Scraper - Quotes Scraper")
    print("=" * 50)
    print(f"🌐 Scraping from: {BASE_URL}")
    print(f"📄 Pages to scrape: {max_pages}\n")
    
    for page_num in range(1, max_pages + 1):
        url = f"{BASE_URL}/page/{page_num}/"
        print(f"⏳ Scraping page {page_num}...", end=" ")
        
        try:
            # Request send cheyyi
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()
            
            # HTML parse cheyyi
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Quotes find cheyyi
            quote_blocks = soup.find_all("div", class_="quote")
            
            if not quote_blocks:
                print("No more quotes found. Stopping.")
                break
            
            for block in quote_blocks:
                text   = block.find("span", class_="text").get_text(strip=True)
                author = block.find("small", class_="author").get_text(strip=True)
                tags   = [tag.get_text() for tag in block.find_all("a", class_="tag")]
                tags_str = ", ".join(tags)
                
                all_quotes.append({
                    "Quote": text,
                    "Author": author,
                    "Tags": tags_str,
                    "Page": page_num
                })
            
            print(f"✅ {len(quote_blocks)} quotes found!")
        
        except requests.exceptions.ConnectionError:
            print(f"\n❌ Connection Error! Check your internet connection.")
            break
        except requests.exceptions.Timeout:
            print(f"\n❌ Timeout! Website took too long to respond.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            break
    
    return all_quotes

def save_to_csv(quotes):
    """Quotes CSV lo save cheyyi"""
    
    if not quotes:
        print("\n⚠️  No data to save!")
        return
    
    with open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["Quote", "Author", "Tags", "Page"])
        writer.writeheader()
        writer.writerows(quotes)
    
    print(f"\n💾 Data saved to '{OUTPUT_FILE}'")

def display_sample(quotes, count=5):
    """Sample quotes terminal lo show cheyyi"""
    
    print(f"\n📊 Sample Output (First {count} quotes):")
    print("-" * 60)
    
    for i, q in enumerate(quotes[:count], 1):
        print(f"\n{i}. 💬 {q['Quote'][:80]}...")
        print(f"   ✍️  Author : {q['Author']}")
        print(f"   🏷️  Tags   : {q['Tags']}")

def show_stats(quotes):
    """Stats show cheyyi"""
    
    print("\n" + "=" * 50)
    print("   📈 Scraping Summary")
    print("=" * 50)
    print(f"✅ Total Quotes Scraped : {len(quotes)}")
    
    # Unique authors
    authors = set(q['Author'] for q in quotes)
    print(f"👤 Unique Authors       : {len(authors)}")
    
    # Most common author
    from collections import Counter
    author_counts = Counter(q['Author'] for q in quotes)
    top_author = author_counts.most_common(1)[0]
    print(f"🏆 Most Quoted Author   : {top_author[0]} ({top_author[1]} quotes)")
    print(f"📁 Output File          : {OUTPUT_FILE}")
    print(f"🕐 Scraped At           : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)

def main():
    print("\n🕷️  Starting Web Scraper...\n")
    
    # Pages count user nundi teesuko
    try:
        pages = int(input("How many pages to scrape? (1-10, default=3): ").strip() or "3")
        pages = max(1, min(pages, 10))  # 1 to 10 range
    except ValueError:
        pages = 3
    
    print()
    
    # Scrape cheyyi
    quotes = scrape_quotes(max_pages=pages)
    
    if quotes:
        # Sample show cheyyi
        display_sample(quotes)
        
        # CSV lo save cheyyi
        save_to_csv(quotes)
        
        # Stats show cheyyi
        show_stats(quotes)
        
        print(f"\n🎉 Scraping complete! Check '{OUTPUT_FILE}' for full data.")
    else:
        print("\n❌ No data scraped. Check internet connection.")

if __name__ == "__main__":
    main()