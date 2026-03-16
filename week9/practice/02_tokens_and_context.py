"""
Week 9: How LLMs Work
Topic: Tokens and Context Windows

Tokens are the basic units LLMs work with. Understanding tokenization
helps you reason about input limits, costs, and strange LLM behaviors.
"""

# Exercise 1: What are tokens?
# Tokens are not words. They are sub-word pieces. A word like "unhappiness"
# might be split into ["un", "happiness"] or ["un", "happi", "ness"].
# TODO: Run this to see how text splits into tokens at a basic level.

def simple_tokenize(text):
    """A naive whitespace + punctuation tokenizer.

    Real LLMs use BPE (Byte Pair Encoding) which is much more sophisticated.
    This is just to illustrate the concept of breaking text into pieces.
    """
    import re
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens


sample_texts = [
    "Hello, world!",
    "The cat sat on the mat.",
    "LLM testing is fundamentally different from traditional testing.",
    "GPT-5.4 uses approximately 200K tokens as its context window.",
]

print("--- Simple Tokenization ---")
for text in sample_texts:
    tokens = simple_tokenize(text)
    print(f"  Text: '{text}'")
    print(f"  Tokens ({len(tokens)}): {tokens}")
    print()


# Exercise 2: Token counting matters
# LLMs have a maximum context window (input + output tokens).
# Going over the limit means truncation or errors.
# TODO: Study why token counting is critical for test design.

def estimate_tokens(text):
    """Rough estimate: ~4 characters per token for English text.

    This is a very rough heuristic. For accurate counting, use tiktoken.
    """
    return len(text) // 4


# Context window sizes for major models (as of March 2026)
model_context_windows = {
    "GPT-5.4": 200_000,
    "Claude 4.x (Opus)": 200_000,
    "Claude 4.x (Sonnet)": 200_000,
    "Gemini 3.1 Pro": 2_000_000,
}

print("--- Context Window Sizes ---")
for model, window in model_context_windows.items():
    print(f"  {model}: {window:,} tokens")

print()

# Calculate how much text fits in each window
sample_long_text = "This is a sample sentence for estimation. " * 100
estimated = estimate_tokens(sample_long_text)
print(f"Sample text length: {len(sample_long_text)} characters")
print(f"Estimated tokens: ~{estimated}")
print()


# Exercise 3: Why context windows matter for testing
# TODO: Think about how context windows affect test design.

context_window_testing = [
    "Test inputs that approach the context limit",
    "Test what happens when input is truncated",
    "Test with very short vs very long inputs",
    "Test that the model uses information from early in a long context",
    "Consider cost: longer inputs = more tokens = more money",
]

print("--- Context Window Testing Checklist ---")
for i, item in enumerate(context_window_testing, 1):
    print(f"  {i}. {item}")

print()
print("Key takeaway: Tokens are the currency of LLMs.")
print("Every token costs money, takes time, and counts toward the limit.")
print("A good tester thinks in tokens, not words.")
