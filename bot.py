import snscrape.modules.twitter as sntwitter
from openai import OpenAI
import time
from config import OPENAI_API_KEY

# Set up OpenAI API client
client = OpenAI(api_key=OPENAI_API_KEY)

def get_thread(url, max_retries=5, backoff_factor=1):
    tweet_id = url.split('/')[-1].split('?')[0]
    query = f'conversation_id:{tweet_id}'

    for attempt in range(max_retries):
        try:
            thread = []
            for tweet in sntwitter.TwitterSearchScraper(query).get_items():
                if tweet.conversationId == int(tweet_id):
                    thread.append(tweet.content)
            return thread[::-1]
        except sntwitter.ScraperException as e:
            if attempt < max_retries - 1:
                wait_time = backoff_factor * (2 ** attempt)
                print(f"Scraping failed, retrying in {wait_time} seconds...")
                time.sleep(wait_time)
            else:
                print("Max retries reached. Exiting.")
                raise e

def summarize_thread(thread):
    text = " ".join(thread)
    prompt = f"Summarize the following twitter thread:\n\n{text}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an AI assistant, skilled in summarizing threads into concise and informative bullet points."},\
            {"role": "user", "content": prompt},
        ],
    )
    summary = completion.choices[0].message['content'].strip()
    return summary

if __name__ == "__main__":
    url = input("Enter the URL of the Twitter thread: ")
    try:
        thread = get_thread(url)
        summary = summarize_thread(thread)
        print(f"TL;DR: {summary}")
    except Exception as e:
        print(f"Failed to retrieve and summarize thread: {e}")
