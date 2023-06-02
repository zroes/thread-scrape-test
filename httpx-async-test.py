# import asyncio
# from aiohttp import ClientSession
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options


# async def send_request(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             print(f"Response from {url}: {response.status}")


# async def run_requests(urls):
#     tasks = []
#     for url in urls:
#         task = asyncio.ensure_future(send_request(url))
#         tasks.append(task)
#     await asyncio.gather(*tasks)


# # Set up Selenium with a headless Chrome browser
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(options=chrome_options)

# # Define the list of URLs
# urls = [
#     'https://www.traderjoes.com/home/search?q=chicken&section=products&global=yes',
#     'https://www.albertsons.com/shop/search-results.html?q=chicken',
# ]

# # Run the script
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run_requests(urls))

# # Close the Selenium driver
# driver.quit()
