# sentiment_analysis.py
import os
import json
import datetime
import requests
import pandas as pd
from transformers import pipeline

def collect_perplexity_sentiment(ticker, api_key=None):
    """
    Collect real-time sentiment data using the Perplexity API.

    Parameters:
        ticker (str): Stock ticker symbol.
        api_key (str): Perplexity API key.

    Returns:
        pd.DataFrame: DataFrame containing the Perplexity API response.
    """
    if not api_key:
        print("No Perplexity API key provided")
        return pd.DataFrame()
    
    print(f"Collecting real-time sentiment data for {ticker} using Perplexity API")
    
    query = (
        f"Scrape the latest financial news articles covering {ticker} and recent economic events impacting "
        "financial markets. Focus on capturing actionable insights related to market sentiment, investor "
        "reactions, earnings reports, trading strategies, and macroeconomic indicators."
    )
    
    url = "https://api.perplexity.ai/chat/completions"
    payload = {
        "model": "sonar",
        "messages": [
            {
                "role": "system",
                "content": "You are a financial analyst specializing in stock market sentiment analysis. Provide detailed insights with factual information."
            },
            {
                "role": "user",
                "content": query
            }
        ],
        "temperature": 0.2,
        "top_p": 0.9,
        "max_tokens": 1500,
        "search_domain_filter": None,
        "return_citations": True,
        "return_related_questions": False,
        "stream": False
    }
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    results = []
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            content = response_data['choices'][0]['message']['content']
            citations = response_data.get('citations', [])
            result = {
                "ticker": ticker,
                "timestamp": datetime.datetime.now(),
                "response": content,
                "citations": json.dumps(citations),
                "model": response_data.get("model", "sonar"),
                "tokens_used": response_data.get("usage", {}).get("total_tokens", 0)
            }
            results.append(result)
            print(f"Successfully retrieved Perplexity data for {ticker}")
        else:
            print(f"Error: API request failed with status code {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error querying Perplexity API: {e}")
    
    if results:
        perplexity_df = pd.DataFrame(results)
        output_file = f"{ticker}_perplexity_responses.csv"
        perplexity_df.to_csv(output_file, index=False)
        print(f"Perplexity responses saved to {output_file}")
        return perplexity_df
    else:
        print("No results from Perplexity API")
        return pd.DataFrame()

def analyze_perplexity_sentiment(perplexity_df, ticker):
    """
    Analyze sentiment from Perplexity API responses using FinBERT.

    Parameters:
        perplexity_df (pd.DataFrame): DataFrame containing Perplexity responses.
        ticker (str): Stock ticker symbol.

    Returns:
        pd.DataFrame: DataFrame summarizing the sentiment analysis.
    """
    if perplexity_df.empty:
        print("No Perplexity data to analyze")
        return pd.DataFrame()
    
    print(f"Analyzing Perplexity sentiment data for {ticker}")
    finbert = pipeline("sentiment-analysis", model="ProsusAI/finbert", tokenizer="ProsusAI/finbert")
    
    def analyze_chunk(text):
        if pd.isna(text) or text == "":
            return {"score": 0.5, "label": "neutral"}
        # Split text into manageable chunks (max 512 characters)
        chunks = [text[i:i+512] for i in range(0, len(text), 512)]
        scores = []
        labels = []
        for chunk in chunks:
            try:
                result = finbert(chunk)[0]
                scores.append(result["score"])
                labels.append(result["label"])
            except Exception as e:
                print(f"Error in FinBERT analysis: {e}")
        if not scores:
            return {"score": 0.5, "label": "neutral"}
        avg_score = sum(scores) / len(scores)
        pos_count = labels.count("positive")
        neg_count = labels.count("negative")
        neu_count = labels.count("neutral")
        if pos_count > neg_count and pos_count > neu_count:
            dominant_label = "positive"
        elif neg_count > pos_count and neg_count > neu_count:
            dominant_label = "negative"
        else:
            dominant_label = "neutral"
        return {"score": avg_score, "label": dominant_label}
    
    sentiment_results = perplexity_df["response"].apply(analyze_chunk)
    perplexity_df["sentiment_score"] = sentiment_results.apply(lambda x: x["score"])
    perplexity_df["sentiment_label"] = sentiment_results.apply(lambda x: x["label"])
    
    def extract_key_insights(text):
        if pd.isna(text) or text == "":
            return ""
        sentences = text.split(".")
        return ". ".join(sentences[:3]) + "."
    
    perplexity_df["key_insights"] = perplexity_df["response"].apply(extract_key_insights)
    perplexity_df["date"] = pd.to_datetime(perplexity_df["timestamp"]).dt.date
    
    sentiment_result = pd.DataFrame({
        "date": [pd.to_datetime(perplexity_df["date"].iloc[0])],
        "perplexity_sentiment_avg": [perplexity_df["sentiment_score"].mean()],
        "perplexity_sentiment_label": [perplexity_df["sentiment_label"].iloc[0]],
        "perplexity_key_insights": [perplexity_df["key_insights"].iloc[0]],
        "perplexity_query_count": [len(perplexity_df)],
        "perplexity_tokens_used": [perplexity_df["tokens_used"].sum()],
        "perplexity_citations_count": [perplexity_df["citations"].apply(lambda x: len(json.loads(x)) if isinstance(x, str) else 0).sum()]
    })
    
    if sentiment_result["perplexity_sentiment_avg"].iloc[0] > 1:
        sentiment_result["perplexity_sentiment_avg"] = sentiment_result["perplexity_sentiment_avg"] / 5.0
    
    output_file = f"{ticker}_perplexity_sentiment.csv"
    sentiment_result.to_csv(output_file, index=False)
    print(f"Perplexity sentiment analysis saved to {output_file}")
    return sentiment_result

def run_perplexity_sentiment_pipeline(ticker, api_key=None):
    """
    Run the complete sentiment analysis pipeline:
      1. Check for cached sentiment data for today.
      2. If not available, collect data via Perplexity API.
      3. Analyze sentiment using FinBERT.
    
    Parameters:
        ticker (str): Stock ticker symbol.
        api_key (str): Perplexity API key.
    
    Returns:
        pd.DataFrame: DataFrame with sentiment analysis results.
    """
    today = datetime.date.today().strftime("%Y-%m-%d")
    cache_file = f"{ticker}_perplexity_sentiment.csv"
    
    if os.path.exists(cache_file):
        cached_data = pd.read_csv(cache_file)
        if "date" in cached_data.columns:
            cached_data["date"] = pd.to_datetime(cached_data["date"])
            if not cached_data.empty and (cached_data["date"].dt.date == datetime.date.today()).any():
                print(f"Using cached Perplexity sentiment data from today ({today})")
                return cached_data
    
    perplexity_df = collect_perplexity_sentiment(ticker, api_key=api_key)
    sentiment_result = analyze_perplexity_sentiment(perplexity_df, ticker)
    return sentiment_result

if __name__ == "__main__":
    ticker = "AAPL"
    api_key = "your_perplexity_api_key_here"  # Replace with your actual API key
    sentiment_data = run_perplexity_sentiment_pipeline(ticker, api_key)
    print("\nPerplexity Sentiment Analysis Results:")
    print(sentiment_data)
