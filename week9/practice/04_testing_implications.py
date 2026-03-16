"""
Week 9: How LLMs Work
Topic: Testing Implications

Pulling together all the concepts from this week and connecting them
to practical testing decisions you will make throughout this journey.
"""

# Exercise 1: Training vs Inference
# Training: The model learns patterns from data (months, millions of dollars).
# Inference: The model generates output from your input (milliseconds, fractions of a cent).
# As testers, we only interact with inference. But understanding training helps
# us understand WHY the model behaves the way it does.
# TODO: Study these concepts and their implications.

training_vs_inference = {
    "Training": {
        "what": "Model learns patterns from billions of text examples",
        "when": "Done by the model provider (OpenAI, Anthropic, Google)",
        "cost": "Millions of dollars, weeks of compute",
        "tester_concern": "We cannot change this. We test what was trained.",
    },
    "Inference": {
        "what": "Model generates output from your input prompt",
        "when": "Every time you call the API",
        "cost": "Fractions of a cent per call (depends on tokens)",
        "tester_concern": "This is where we operate. We control the input.",
    },
}

print("--- Training vs Inference ---")
for phase, details in training_vs_inference.items():
    print(f"\n  {phase}:")
    for key, value in details.items():
        print(f"    {key}: {value}")


# Exercise 2: The tester's mental model
# TODO: Review this mental model for how LLMs work from a testing perspective.

print("\n\n--- The Tester's Mental Model ---")

mental_model = """
  INPUT (prompt)
    |
    v
  [Tokenizer] --> tokens (sub-word pieces)
    |
    v
  [Model] --> probability distribution over all possible next tokens
    |
    v
  [Sampling] --> pick a token (influenced by temperature, top_p)
    |
    v
  [Repeat] --> feed token back, generate next one
    |
    v
  OUTPUT (response)

  What you CONTROL as a tester:
  - The input prompt (content, length, format)
  - Temperature (0 to 2.0)
  - top_p (0 to 1.0)
  - max_tokens (output length limit)
  - The model version (GPT-5.4, Claude 4.x, Gemini 3.1, etc.)

  What you CANNOT control:
  - The training data
  - The model weights
  - Internal reasoning steps
  - Exact probability distributions
"""
print(mental_model)


# Exercise 3: Key concepts checklist
# TODO: For each concept, write a one-sentence explanation in your own words.
#       Replace the "..." with your explanation.

concepts = {
    "Token": "...",              # What is a token?
    "Context Window": "...",     # What is the context window?
    "Temperature": "...",        # What does temperature do?
    "top_p": "...",              # What does top_p do?
    "Non-determinism": "...",    # Why are LLM outputs non-deterministic?
    "Hallucination": "...",      # What is a hallucination? (preview)
    "Prompt": "...",             # What is a prompt?
    "Inference": "...",          # What happens during inference?
}

print("--- Concept Checklist (fill in your own explanations) ---")
for concept, explanation in concepts.items():
    status = "TODO" if explanation == "..." else "Done"
    print(f"  [{status}] {concept}: {explanation}")


# Exercise 4: Testing scenarios from LLM behavior
# TODO: For each behavior, think about how you would test for it.

print("\n\n--- Testing Scenarios ---")

scenarios = [
    {
        "behavior": "Same prompt, different outputs each time",
        "caused_by": "Non-zero temperature, random sampling",
        "test_approach": "Run N times, check output distribution, use similarity metrics",
    },
    {
        "behavior": "Output gets cut off mid-sentence",
        "caused_by": "max_tokens limit reached",
        "test_approach": "Test with varying max_tokens, check for complete sentences",
    },
    {
        "behavior": "Model ignores instructions at the end of a long prompt",
        "caused_by": "Context window attention distribution (recency vs primacy)",
        "test_approach": "Test instruction placement: beginning, middle, end of prompt",
    },
    {
        "behavior": "Model confidently states incorrect facts",
        "caused_by": "Hallucination (pattern matching without factual grounding)",
        "test_approach": "Compare outputs against known facts, use claim extraction",
    },
    {
        "behavior": "Different models give very different answers",
        "caused_by": "Different training data, different architectures",
        "test_approach": "Multi-provider testing, compare quality across models",
    },
]

for i, scenario in enumerate(scenarios, 1):
    print(f"\n  Scenario {i}: {scenario['behavior']}")
    print(f"    Caused by: {scenario['caused_by']}")
    print(f"    Test approach: {scenario['test_approach']}")

print("\n\nKey takeaway: Understanding WHY LLMs behave this way")
print("directly informs HOW you design your tests.")
