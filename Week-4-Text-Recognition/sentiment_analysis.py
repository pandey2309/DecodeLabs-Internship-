from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

print("=" * 60)
print("          AI TEXT SENTIMENT ANALYZER")
print("=" * 60)

analyzer = SentimentIntensityAnalyzer()

while True:
    text = input("\nEnter a sentence (or type 'exit' to quit): ")

    if text.lower() == "exit":
        print("\nThank you for using AI Text Sentiment Analyzer!")
        break

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    print("\nSentiment Scores:")
    print(scores)

    if compound >= 0.30:
        print("\nSentiment: Positive 😊")

    elif compound <= -0.30:
        print("\nSentiment: Negative 😔")

    else:
        print("\nSentiment: Neutral 😐")