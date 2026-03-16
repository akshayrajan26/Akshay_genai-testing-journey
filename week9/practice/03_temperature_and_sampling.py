"""
Week 9: How LLMs Work
Topic: Temperature and Sampling

Temperature controls how "random" or "focused" the model's output is.
This is one of the most important parameters a tester needs to understand.
"""

import math
import random

# Exercise 1: What temperature does to probabilities
# Temperature modifies the probability distribution before sampling.
# Low temperature = more focused (picks the most likely token)
# High temperature = more random (spreads probability across tokens)
# TODO: Run this and observe how temperature changes the distribution.


def apply_temperature(logits, temperature):
    """Apply temperature scaling to a set of logits (raw model scores).

    Temperature = 1.0: original distribution
    Temperature < 1.0: sharper distribution (more deterministic)
    Temperature > 1.0: flatter distribution (more random)
    Temperature -> 0: always picks the highest probability token (greedy)

    Args:
        logits: Dictionary of token -> raw score.
        temperature: Float controlling randomness.

    Returns:
        Dictionary of token -> adjusted probability.
    """
    if temperature == 0:
        # Greedy: give all probability to the top token
        max_token = max(logits, key=logits.get)
        return {t: (1.0 if t == max_token else 0.0) for t in logits}

    # Apply temperature: divide logits by temperature, then softmax
    scaled = {t: score / temperature for t, score in logits.items()}

    # Softmax to convert to probabilities
    max_val = max(scaled.values())
    exp_vals = {t: math.exp(v - max_val) for t, v in scaled.items()}
    total = sum(exp_vals.values())
    probs = {t: v / total for t, v in exp_vals.items()}
    return probs


# Raw logits (scores before softmax) for possible next tokens
raw_logits = {
    "Paris": 5.0,
    "London": 3.0,
    "Berlin": 2.0,
    "Tokyo": 1.5,
    "Pizza": 0.5,
}

print("--- Temperature Effects ---")
print(f"Raw logits: {raw_logits}")
print()

for temp in [0, 0.1, 0.5, 1.0, 1.5, 2.0]:
    probs = apply_temperature(raw_logits, temp)
    formatted = {t: f"{p:.3f}" for t, p in probs.items()}
    print(f"  Temperature {temp}: {formatted}")

print()
print("Notice: At temperature 0, only 'Paris' has probability.")
print("At temperature 2.0, even 'Pizza' has a reasonable chance.")


# Exercise 2: Sampling with different temperatures
# TODO: Run this and see how temperature affects generated text.

def sample_token(probs):
    """Sample a single token from a probability distribution."""
    tokens = list(probs.keys())
    weights = list(probs.values())
    return random.choices(tokens, weights=weights, k=1)[0]


print("\n--- Sampling at Different Temperatures ---")
for temp in [0.0, 0.3, 0.7, 1.0, 1.5]:
    probs = apply_temperature(raw_logits, temp)
    samples = [sample_token(probs) for _ in range(20)]
    unique = len(set(samples))
    print(f"  Temp {temp}: {samples[:10]}... ({unique} unique in 20 samples)")


# Exercise 3: Top-p (nucleus) sampling
# Instead of using all tokens, top-p only considers the smallest set
# of tokens whose cumulative probability exceeds p.
# TODO: Study how top-p differs from temperature.

def top_p_filter(probs, p=0.9):
    """Keep only tokens whose cumulative probability reaches p.

    This prevents sampling very unlikely tokens while still allowing
    reasonable variety.
    """
    sorted_tokens = sorted(probs.items(), key=lambda x: x[1], reverse=True)
    cumulative = 0.0
    filtered = {}
    for token, prob in sorted_tokens:
        cumulative += prob
        filtered[token] = prob
        if cumulative >= p:
            break

    # Re-normalize
    total = sum(filtered.values())
    return {t: p / total for t, p in filtered.items()}


print("\n--- Top-p Filtering ---")
probs_t1 = apply_temperature(raw_logits, 1.0)
print(f"  Original probs (temp=1.0): { {t: f'{p:.3f}' for t, p in probs_t1.items()} }")

for p_val in [0.5, 0.8, 0.95]:
    filtered = top_p_filter(probs_t1, p=p_val)
    print(f"  Top-p={p_val}: { {t: f'{p:.3f}' for t, p in filtered.items()} }")


# Exercise 4: Testing implications of temperature
# TODO: Add your own notes to this list.

print("\n--- Testing Implications ---")
implications = [
    "Temperature 0 gives deterministic output (good for regression tests)",
    "Temperature > 0 means repeated runs give different results",
    "Tests must use statistical methods (run N times, check distributions)",
    "Always log the temperature used in each test run",
    "Low temperature favors common/safe answers, high favors creative/risky",
    "top_p and temperature interact: understand both before testing",
]
for i, item in enumerate(implications, 1):
    print(f"  {i}. {item}")
