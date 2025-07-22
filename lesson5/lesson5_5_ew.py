import asyncio
from crawl4ai import (AsyncWebCrawler, CrawlerRunConfig,CacheMode)
from crawl4ai.extraction_strategy import JsonCssExtractionStrategy

async def main():
    raw_html="""<html>
    <head>
        <title>測試網頁</title>
    </head>
    <body>
        <div class='item'>
            <h2>項目1</h2>
            <a href='https://example.com/item1'>連結1</a>
        </div>
    </body>
    </html>    """

    schema = {
        "name":"範例項目",
        "baseSelector":"div.item",
        "fields":[
            {
                "name":"產品",
                "selector":"h2",
                "type":"text"
            },
            {
                "name":"連結",
                "selector":"a",
                "type":"attribute",
                "attribute":"href"
            }
        ]
    }

    #CrawlerRunConfig 實體
    run_config = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,  # 不使用快取
        extraction_strategy=JsonCssExtractionStrategy(schema=schema)
    )

    #建立一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        result = await crawler.arun(
            url=f"raw://{raw_html}",
            config=run_config
        )
        print(type(result.extracted_content)) 
        print(result.extracted_content)

if __name__ == "__main__":
    #使用 asyncio.run() 來執行 main 函數
    #這樣可以確保事件循環正確運行
    #如果在 Jupyter Notebook 中，可能需要使用 nest_asyncio.apply() 來解決事件循環問題
    # import nest_asyncio
    # nest_asyncio.apply()  # 解決 asyncio 的事件循環問題
    
    asyncio.run(main())

# await main()
