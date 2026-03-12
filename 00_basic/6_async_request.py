import aiohttp
import asyncio
import time
import ssl


# 异步请求单个网页（新增 SSL 验证关闭）
async def async_request_url(url):
    # 创建忽略 SSL 验证的上下文
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    async with aiohttp.ClientSession() as session:
        # 发起请求时指定 ssl=ssl_context
        async with session.get(url, ssl=ssl_context) as resp:
            return url, resp.status


async def async_request():
    urls = [
        "https://www.baidu.com",
        "https://www.taobao.com",
        "https://www.jd.com",
        "https://www.tianmao.com",
        "https://bilibili.com"
    ]
    start = time.time()
    tasks = [async_request_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, status in results:
        print(f"异步：{url} 响应状态码：{status}")
    print(f"异步总耗时：{time.time() - start:.2f}秒")


# 运行前需导入 ssl 模块


asyncio.run(async_request())
