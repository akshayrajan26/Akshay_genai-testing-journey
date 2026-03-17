"""Prompt analyzer -- estimates token count and flags potential issues.

A simple utility to check prompts before sending them to an LLM.
This becomes a tool you can reuse when working with real APIs later.
"""


# Context window sizes (tokens) for major models as of March 2026
MODEL_LIMITS = {
    "GPT-5.4": 200_000,
    "Claude 4.x": 200_000,
    "Gemini 3.1 Pro": 2_000_000,
}


def analyze_prompt(text):
    """Analyze a prompt and print a summary of potential issues.

    Args:
        text: The prompt text to analyze.
    """
    char_count = len(text)
    estimated_tokens = max(1, char_count // 4)  # Rough: ~4 chars per token
    word_count = len(text.split())

    print(f"  Prompt: '{text[:60]}{'...' if len(text) > 60 else ''}'")
    print(f"  Characters: {char_count:,}")
    print(f"  Words: {word_count:,}")
    print(f"  Estimated tokens: ~{estimated_tokens:,}")

    # Check against model limits
    for model, limit in MODEL_LIMITS.items():
        usage_pct = (estimated_tokens / limit) * 100
        if usage_pct > 80:
            print(f"  WARNING: Uses ~{usage_pct:.0f}% of {model} context window")
        elif usage_pct > 50:
            print(f"  Note: Uses ~{usage_pct:.0f}% of {model} context window")

    # Flag if too short (might get vague answers)
    if word_count < 5:
        print("  Tip: Very short prompt -- consider adding more context")

    # Flag if very long
    if estimated_tokens > 100_000:
        print("  Tip: Very long prompt -- watch for 'lost in the middle' effect")
