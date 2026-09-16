
from transformers import pipeline

classifier = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

def sentiment_analysis(text):

    prompt = f"""
You are a sentiment analysis system.

Classify the sentiment of this text:

"{text}"

Possible labels:
1. Positive
2. Negative
3. Neutral

Answer with ONLY the label.
"""

    output = classifier(
        prompt,
        max_new_tokens=5,
        do_sample=False
    )

    response = output[0]["generated_text"]

    generated = response[len(prompt):].strip()

    print("--------------------------------")
    print("Text      :", text)
    print("Sentiment :", generated)
    print("--------------------------------")


# Test cases
sentiment_analysis(
    "The movie was amazing and I really enjoyed it."
)

sentiment_analysis(
    "The service was horrible and very disappointing."
)

sentiment_analysis(
    "The package arrived this morning."
)