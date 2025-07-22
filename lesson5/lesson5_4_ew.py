import asyncio
from crawl4ai import (AsyncWebCrawler,
                      CrawlerRunConfig,
                      DefaultMarkdownGenerator,
                      PruningContentFilter)


async def main():
    #設定爬蟲的配置
    run_config = CrawlerRunConfig( 
            markdown_generator=DefaultMarkdownGenerator(
                #設定Markdown生成器的配置
                content_filter=PruningContentFilter(
                    threshold=0.5,
                    threshold_type='fixed',
                    min_word_count=50)
                    ),
            excluded_tags=['nav', 'footer', 'header', 'aside','form'],
            css_selectors='article, .content, .post-content, .entry-content, main'

    )

    #一個AsyncWebCrawler的實體
    async with AsyncWebCrawler() as crawler:
        #Run the crawler on a URL
        url='https://blockcast.it/2025/07/21/eths-most-hated-rally-could-trigger-331m-in-liquidations/'
        result = await crawler.arun(
                url=url,
                config=run_config
                )
        print(type(result))
        print("=" * 20)
        #列印取出的結果
        print(result.markdown)
      

if __name__ == "__main__":
    #使用 asyncio.run() 來執行 main 函數
    #這樣可以確保事件循環正確運行
    #如果在 Jupyter Notebook 中，可能需要使用 nest_asyncio.apply() 來解決事件循環問題
    # import nest_asyncio
    # nest_asyncio.apply()  # 解決 asyncio 的事件循環問題
    
    asyncio.run(main())

# await main()
