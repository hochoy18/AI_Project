import requests
import time

base_urls = [
        "https://www.baidu.com",
        "https://www.taobao.com",
        "https://www.jd.com",
        "https://www.google.com",
        "https://chatgpt.com"
    ]
# 同步请求3个网页（模拟IO密集型任务）
def sync_request(urls):
    start = time.time()
    for url in urls:
        resp = requests.get(url)  # 阻塞：等待网页响应
        print(f"同步：{url} 响应状态码：{resp.status_code}")
    print(f"同步总耗时：{time.time() - start:.2f}秒")


if __name__ == "__main__":
    sync_request(base_urls)
# 输出（总耗时约3秒，因为逐个等待）：
# 同步：https://www.baidu.com 响应状态码：200
# 同步：https://www.taobao.com 响应状态码：200
# 同步：https://www.jd.com 响应状态码：200
# 同步总耗时：3.05秒