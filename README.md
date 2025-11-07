# Ella v4.0
Ahh just Instagram & Threads 5-Letter Username Finder  
Author: Reinhart  
Portfolio: [www.reinhart.pages.dev](https://www.reinhart.pages.dev)  
Telegram: [@kiri0507](https://t.me/kiri0507)

---

## Description

Ella is a high-speed tool to find and check the availability of 5-letter usernames on Instagram and Threads.  
It uses concurrency and proxies for speed, with live status output and Telegram bot notifications when available usernames are found.

---

## Features

- Checks 5-letter username availability.
- Uses concurrent proxy checking (default 2000 concurrency).
- Sends Telegram notification for each available username.
- Displays real-time statistics: checked count, hits, checks per second.
- Proxy warming and validation.

---

## Installation

1. **Clone the repo:**
    ```bash
    git clone https://github.com/Reinhart-py/Ella.git
    cd Ella
    ```

2. **Install dependencies:**
    ```
    pip install aiohttp
    ```

3. **Prepare your proxies:**
    - Create a file called `proxies.txt` in the root folder.
    - Add your HTTP proxies (one per line), e.g.
      ```
      45.89.XX.123:8080
      176.59.XX.214:3128
      104.17.XX.47:80
      ```

4. **Get your Telegram Bot API key and Chat ID:**
    - Create a bot at [BotFather](https://t.me/BotFather)
    - Get your **Bot Token** (`123456789:ABCDEF...`)
    - Send a message to your bot, then use [userinfobot](https://t.me/userinfobot) to get your chat ID.

---

## Usage

1. **Run the tool:**
    ```bash
    python 5l.py
    ```

2. **Follow the prompts:**
    - Enter your Telegram chat ID
    - Enter your bot token

3. **Live output:**
    - Current hits (available usernames found)
    - Checked count (usernames tested)
    - Checks per second ("speed")
    - Available usernames are sent to your Telegram chat

---

## Notes

- **Proxies**  
  - Only HTTP proxies are supported.
  - Tool will check every proxy and use only the working ones.
  - If no working proxies are found, the tool will stop.

- **Rate Limiting**  
  - High concurrency settings may get your proxies blocked/flooded.  
    Use a larger proxy list for better results.

- **Telegram Notification**  
  - Each available username sends a new message to your Telegram.

---

## Troubleshooting

- If you see `proxies.txt is missing or empty`, ensure your proxies.txt exists and has valid entries.
- Make sure your Telegram bot is active and you provided the correct chat ID and token.
- If no proxies work, consider changing your proxy sources.

---

## License

For personal use and educational purposes only.  
Not affiliated with Instagram or Meta.

---

## Credit

Coded by Reinhart  
Telegram: [@kiri0507](https://t.me/kiri0507)  
Portfolio: [www.reinhart.pages.dev](https://www.reinhart.pages.dev)

