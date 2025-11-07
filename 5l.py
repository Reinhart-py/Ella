import asyncio
import aiohttp
import random
import string
import time
from uuid import uuid4
from secrets import token_hex

CONCURRENCY = 2000
PROXY_TIMEOUT = 7
PROXY_TEST_URL = 'https://api.ipify.org'

B, E, F, G, W = '\x1b[38;5;208m', '\033[1;31m', '\033[2;32m', '\033[2;36m', '\033[1;37m'

print(f'''
{G}     ,gggg,
{G}   ,d8""8I                          ,dPYb,
{G}  ,d8"  "I                         ,IP'`"I
{G} ,8I     "                         I8  ,"
{G} I8'                               I8 d'
{G} d8                                I8d888b
{G} 88         ,gggg,gg   ,ggg,,ggg,  I8P'"Y8
{G} 88        dP"  "Y8I  ,8" "8P" "8, `8'  `8'
{G} Y8b,___,d8I     I8I  I8   8I   8I  `8'   `8
{G}  "Y88888" "8a_a_8"II  `8, ,8I ,8P'   `8'    `8
{E}-----------------------------------------------
{W}   Tool      : {F}Ella {W}v4.0 (Storm)
{W}   Credit    : {F}Reinhart
{W}   Portfolio : {F}www.reinhart.pages.dev
{W}   Telegram  : {F}@kiri0507
{E}-----------------------------------------------
''')

ID = input(f'{W}ENTER YOUR CHAT ID > {F}')
TOKEN = input(f'{W}ENTER YOUR BOT TOKEN > {F}')
print(f'{E}-----------------------------------------------{W}')

async def notify(s, user, stats):
    stats['hits'] += 1
    text = f"👽 AVAILABLE USERNAME : @{user}"
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    try:
        await s.post(url, params={'chat_id': ID, 'text': text})
    except Exception:
        pass

async def check(s, user, proxy, stats):
    headers = {
        'accept': '*/*', 'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded', 'dpr': '2',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/accounts/emailsignup/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'x-asbd-id': '129477', 'x-csrftoken': token_hex(8)*2, 'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0', 'x-instagram-ajax': '1012280089',
        'x-requested-with': 'XMLHttpRequest',
    }
    data = {'email': 'a@b.c', 'username': user, 'client_id': token_hex(13).upper()}
    url = 'https://www.instagram.com/api/v1/web/accounts/web_create_ajax/attempt/'
    try:
        async with s.post(url, headers=headers, data=data, proxy=proxy, timeout=7) as r:
            text = await r.text()
            if '"dryrun_passed":true' in text:
                await notify(s, user, stats)
    except Exception:
        pass
    finally:
        stats['checked'] += 1

async def reporter(start_time, stats):
    while True:
        elapsed = time.monotonic() - start_time
        rate = stats['checked'] / elapsed if elapsed > 0 else 0
        hits, checked = stats['hits'], stats['checked']
        print(f"{W}Hits: {F}{hits}{W} | Checked: {G}{checked}{W} | Speed: {F}{rate:.0f}/s{W}", end='\r')
        await asyncio.sleep(0.1)

async def test_proxy(s, p):
    try:
        async with s.get(PROXY_TEST_URL, proxy=f"http://{p}", timeout=PROXY_TIMEOUT) as r:
            if r.status == 200: return p
    except Exception: return None

async def run():
    try:
        with open('proxies.txt', 'r') as f:
            proxies_in = [line.strip() for line in f if line.strip()]
        if not proxies_in: raise FileNotFoundError
    except FileNotFoundError:
        print(f"{E}'proxies.txt' is missing or empty. Please add http proxies.")
        return

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as s:
        print(f"{W}Warming up... testing {G}{len(proxies_in)}{W} proxies.")
        tasks = [test_proxy(s, p) for p in proxies_in]
        results = await asyncio.gather(*tasks)
        proxies = [p for p in results if p]

        if not proxies:
            print(f"{E}No working proxies found. Can't continue.")
            return

        print(f"{F}{len(proxies)}{W} proxies are live. Starting the work so thamja jara...")
        print(f'{E}-----------------------------------------------{W}')
        
        stats = {'checked': 0, 'hits': 0}
        start_time = time.monotonic()

        reporter_task = asyncio.create_task(reporter(start_time, stats))
        
        while True:
            user = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            proxy = random.choice(proxies)
            await check(s, user, f"http://{proxy}", stats)
            await asyncio.sleep(1 / CONCURRENCY)

if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print(f"\n{E}Aborted.{W}")
