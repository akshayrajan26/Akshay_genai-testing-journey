"""Main script for the llm-concepts-notebook mini project.

A simple tool that combines a token generation simulator
and a prompt analyzer -- your first LLM testing utilities.
"""

from core.simulator import generate_tokens
from core.analyzer import analyze_prompt


def main():
    print("=" * 50)
    print("  LLM Concepts Notebook")
    print("=" * 50)

    # Part 1: Token Generation Simulator
    print("\n--- Token Generation Simulator ---\n")

    vocab = {
        "mat": 0.40,
        "floor": 0.25,
        "chair": 0.15,
        "roof": 0.10,
        "table": 0.07,
        "moon": 0.03,
    }

    prompt = "The cat sat on the"

    print("Low temperature (focused, deterministic):")
    generate_tokens(prompt, vocab, temperature=0.2, n_runs=5)

    print("\nHigh temperature (creative, random):")
    generate_tokens(prompt, vocab, temperature=1.5, n_runs=5)

    # Part 2: Prompt Analyzer
    print("\n--- Prompt Analyzer ---\n")

    prompts = [
        "What is Python?",
        "Explain the difference between lists and tuples in Python. "
        "Include examples for each and describe when to use one over the other.",
        "A" * 800_000,  # Very long input
    ]

    for prompt in prompts:
        analyze_prompt(prompt)
        print()


if __name__ == "__main__":
    main()
