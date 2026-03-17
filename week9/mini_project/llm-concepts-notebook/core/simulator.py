"""Token generation simulator with temperature control.

Simulates how LLMs pick the next token from a probability distribution.
Reuses the temperature and sampling concepts from the practice files.
"""

import math
import random


def generate_tokens(prompt, vocab, temperature=1.0, n_runs=5):
    """Simulate LLM token generation with temperature control.

    Args:
        prompt: The input text (context).
        vocab: Dict of possible next tokens and their base probabilities.
        temperature: Controls randomness (0=greedy, 1=normal, >1=creative).
        n_runs: How many times to generate.
    """
    # Apply temperature to the probabilities
    adjusted = _apply_temperature(vocab, temperature)

    tokens = list(adjusted.keys())
    weights = list(adjusted.values())

    print(f"  Prompt: '{prompt}'")
    print(f"  Temperature: {temperature}")

    results = []
    for i in range(n_runs):
        selected = random.choices(tokens, weights=weights, k=1)[0]
        results.append(selected)
        print(f"    Run {i + 1}: {prompt} {selected}")

    unique = len(set(results))
    print(f"  -> {unique} unique tokens in {n_runs} runs")
    return results


def _apply_temperature(vocab, temperature):
    """Scale probabilities using temperature."""
    if temperature == 0:
        top = max(vocab, key=vocab.get)
        return {t: (1.0 if t == top else 0.0) for t in vocab}

    # Convert probs to logits, scale, then softmax back
    logits = {t: math.log(max(p, 1e-10)) for t, p in vocab.items()}
    scaled = {t: v / temperature for t, v in logits.items()}
    max_val = max(scaled.values())
    exp_vals = {t: math.exp(v - max_val) for t, v in scaled.items()}
    total = sum(exp_vals.values())
    return {t: v / total for t, v in exp_vals.items()}
