import requests
import pyttsx3

def main():
    api_key = '3a5398b1d58845c78115fbe097646aaa'  # Replace with your NewsAPI key
    url = f'https://newsapi.org/v2/top-headlines?country=ca&apiKey={api_key}'

    response = requests.get(url)
    print("Status code:", response.status_code)

    if response.status_code != 200:
        print("Failed to fetch news. Check your API key or network.")
        return

    data = response.json()
    articles = data.get('articles', [])

    if not articles:
        print("No news articles found. Check API key or country parameter.")
        return

    print(f"🗞️ Reading Top {len(articles)} News Headlines:\n")

    engine = pyttsx3.init()

    # Optional: set voice rate (speed) and volume here if you want
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 1.0)  # Volume 0.0 to 1.0

    for i, article in enumerate(articles[:5], start=1):
        title = article.get('title', 'No title available')
        print(f"{i}. {title}")
        engine.say(title)

    engine.runAndWait()

if __name__ == "__main__":
    main()
