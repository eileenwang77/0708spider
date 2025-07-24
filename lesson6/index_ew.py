import wantgoo
import asyncio

def main():
        urls = [
        "https://www.wantgoo.com/stock/2330/technical-chart",
        "https://www.wantgoo.com/stock/2317/technical-chart",
        "https://www.wantgoo.com/stock/2454/technical-chart",
        "https://www.wantgoo.com/stock/2303/technical-chart",
        "https://www.wantgoo.com/stock/2412/technical-chart",
        "https://www.wantgoo.com/stock/2884/technical-chart",
        "https://www.wantgoo.com/stock/2881/technical-chart",
        "https://www.wantgoo.com/stock/2308/technical-chart",
        "https://www.wantgoo.com/stock/2337/technical-chart",
        "https://www.wantgoo.com/stock/2882/technical-chart",
    ]
    results:list[dict] = asyncio.run(get_stock_data(urls=urls))
    for stock in results:
        print(stock)

if __name__ == '__main__':
    main()

# This code is part of a web scraping project using the WantGoo website.