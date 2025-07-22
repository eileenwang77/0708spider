import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        url='https://blockcast.it/2025/07/21/eths-most-hated-rally-could-trigger-331m-in-liquidations/'
        result = await crawler.arun(url=url)
        print(type(result))
        print("=")
        #列印取出的結果
        print(result.markdown)
        print("n"*40)
        print(result.markdown.raw_markdown[:200])

if __name__ == "__main__":
    #使用 asyncio.run() 來執行 main 函數
    #這樣可以確保事件循環正確運行
    #如果在 Jupyter Notebook 中，可能需要使用 nest_asyncio.apply() 來解決事件循環問題
    # import nest_asyncio
    # nest_asyncio.apply()  # 解決 asyncio 的事件循環問題
    
    asyncio.run(main())

# await main()
