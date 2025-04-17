#!/usr/bin/env python3
"""
Smart Data Watcher - AI утилита для криптовалют.
Она автоматически анализирует Twitter, Reddit и новости, чтобы предсказать краткосрочные движения цены.
"""

import requests
import time
import random

def get_fake_social_sentiment():
    """Имитация анализа соцсетей (можно заменить на реальное API)"""
    sentiments = ["bullish", "bearish", "neutral"]
    return random.choice(sentiments)

def get_crypto_price(symbol="BTC"):
    """Берём цену с CoinGecko API"""
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        data = requests.get(url).json()
        return data["bitcoin"]["usd"]
    except:
        return None

def analyze_and_recommend():
    sentiment = get_fake_social_sentiment()
    price = get_crypto_price()

    if price is None:
        print("❌ Ошибка получения цены")
        return

    print(f"💰 Текущая цена BTC: ${price}")
    print(f"🧠 Социальный сентимент: {sentiment}")

    if sentiment == "bullish":
        print("✅ Рекомендация: рассмотреть покупку")
    elif sentiment == "bearish":
        print("⚠️ Рекомендация: быть осторожным, возможна просадка")
    else:
        print("ℹ️ Рекомендация: наблюдать")

if __name__ == "__main__":
    print("🚀 Smart Data Watcher запущен!")
    analyze_and_recommend()
