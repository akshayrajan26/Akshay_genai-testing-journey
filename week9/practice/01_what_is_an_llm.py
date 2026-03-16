"""
Week 9: How LLMs Work
Topic: What is a Language Model?

Language models predict the next token in a sequence. Understanding this
is the foundation for everything you will test.
"""

# Exercise 1: Next token prediction (simulation)
# An LLM is essentially a next-token predictor. Given a sequence of tokens,
# it assigns probabilities to every possible next token and picks one.
# TODO: Study this simplified simulation and understand the concept.

import random


def simple_next_token(context, vocab_with_probs):
    """Simulate next-token prediction with weighted probabilities.

    In a real LLM, a neural network computes these probabilities.
    Here we use a simple dictionary to illustrate the concept.

    Args:
        context: The current text so far.
        vocab_with_probs: A dict mapping possible next tokens to probabilities.

    Returns:
        The selected next token.
    """
    tokens = list(vocab_with_probs.keys())
    weights = list(vocab_with_probs.values())
    selected = random.choices(tokens, weights=weights, k=1)[0]
    return selected


# A tiny "language model" for the phrase "The cat sat on the ___"
next_token_probs = {
    "mat": 0.40,
    "floor": 0.25,
    "chair": 0.15,
    "roof": 0.10,
    "table": 0.07,
    "moon": 0.03,
}

context = "The cat sat on the"
print(f"Context: '{context}'")
print(f"Possible next tokens with probabilities: {next_token_probs}")
print()

# Generate 10 completions to see the distribution
completions = []
for i in range(10):
    token = simple_next_token(context, next_token_probs)
    completions.append(token)
    print(f"  Run {i+1}: '{context} {token}'")

print(f"\nGenerated tokens: {completions}")
print("Notice: the same input can produce different outputs. This is non-determinism.")


# Exercise 2: Autoregressive generation
# LLMs generate text one token at a time, feeding each new token back as input.
# TODO: Run this and observe how a sequence is built token by token.

def autoregressive_generate(start, steps, transition_table):
    """Generate a sequence by predicting one token at a time.

    Each generated token becomes part of the context for the next prediction.
    This is how LLMs generate full sentences.
    """
    sequence = [start]
    current = start
    for step in range(steps):
        if current in transition_table:
            next_token = simple_next_token(current, transition_table[current])
            sequence.append(next_token)
            current = next_token
        else:
            break
    return " ".join(sequence)


# A tiny transition table (like a very small language model)
transitions = {
    "The": {"cat": 0.5, "dog": 0.3, "bird": 0.2},
    "cat": {"sat": 0.6, "ran": 0.3, "slept": 0.1},
    "dog": {"barked": 0.5, "ran": 0.3, "sat": 0.2},
    "bird": {"flew": 0.7, "sang": 0.3},
    "sat": {"quietly": 0.6, "down": 0.4},
    "ran": {"fast": 0.5, "away": 0.5},
}

print("\n--- Autoregressive Generation ---")
for i in range(5):
    result = autoregressive_generate("The", 3, transitions)
    print(f"  Sequence {i+1}: {result}")

print("\nKey takeaway: Each run can produce a different sequence.")
print("This is why LLM testing requires statistical thinking, not exact matching.")


# Exercise 3: Why this matters for testing
# TODO: Read these testing implications and add your own notes.

testing_implications = {
    "Non-determinism": "Same input can give different outputs. Tests must handle this.",
    "Probability-based": "Outputs are sampled from distributions, not looked up.",
    "Context-dependent": "The output depends on the full input context.",
    "Token-level": "LLMs think in tokens, not words. This causes quirks.",
}

print("\n--- Testing Implications ---")
for concept, implication in testing_implications.items():
    print(f"  {concept}: {implication}")
