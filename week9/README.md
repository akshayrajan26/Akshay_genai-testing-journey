# Week 9: How LLMs Work -- Conceptual Foundation

## Week 9 Goal
By end of this week, you will:
- Understand what a language model is and how it generates text
- Explain the difference between training and inference
- Describe tokens, tokenization, and why they matter
- Understand probability-based sampling and why outputs vary
- Explain temperature and its effect on output from a tester's perspective
- Build llm-concepts-notebook (Mini-project)
- Push your ninth deliverable to GitHub

## Daily Breakdown

### Time Budget: 9 hours total
| Day | Focus | Time |
|-----|-------|------|
| Monday | Learn: What is a language model? | 1 hr |
| Tuesday | Learn: Tokens, tokenization, and context windows | 1 hr |
| Wednesday | Learn: Probability, sampling, and temperature | 1 hr |
| Thursday | Learn: Training vs inference, model sizes | 1 hr |
| Friday | Practice: Testing implications of LLM behavior | 1 hr |
| Saturday | Project: Start llm-concepts-notebook | 2 hrs |
| Sunday | Complete mini-project + Push to GitHub | 2 hrs |

## Resources

### YouTube
- [Andrej Karpathy: Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)
- [3Blue1Brown: How LLMs Work](https://www.youtube.com/c/3blue1brown)

### Documentation
- [OpenAI: What are tokens?](https://platform.openai.com/tokenizer)

## Practice Files Guide

Week 9 has 4 practice files to cover everything for the mini-project:

### File 1: `practice/01_what_is_an_llm.py`
**Covers:**
- Language models as next-token predictors
- How text generation works step by step
- Simple simulation of token-by-token generation
- **Time:** 1 hour

### File 2: `practice/02_tokens_and_context.py`
**Covers:**
- What tokens are and why they matter
- Counting tokens with tiktoken
- Context windows and their limits
- **Time:** 1 hour

### File 3: `practice/03_temperature_and_sampling.py`
**Covers:**
- What temperature does to probability distributions
- Greedy decoding vs sampling
- Top-p (nucleus) sampling
- **Time:** 1 hour

### File 4: `practice/04_testing_implications.py`
**Covers:**
- Why LLM outputs are non-deterministic
- How parameter choices affect testability
- Key concepts a tester must understand
- **Time:** 1 hour

# LEARNING TRACK

## Monday: What is a Language Model? (1 hour)

### Watch These Videos
1. **Andrej Karpathy: Intro to Large Language Models**
   - URL: https://www.youtube.com/watch?v=zjkBMFhNj_g
   - Why: The best conceptual introduction to LLMs from a practitioner's perspective.

### Practice Exercises
Run `week9/practice/01_what_is_an_llm.py`.

## Tuesday: Tokens and Context Windows (1 hour)

### Practice Exercises
Run `week9/practice/02_tokens_and_context.py`.

## Wednesday: Temperature and Sampling (1 hour)

### Watch These Videos
1. **3Blue1Brown: How LLMs Work**
   - Why: Visual explanation of probability in language models.

### Practice Exercises
Run `week9/practice/03_temperature_and_sampling.py`.

## Thursday: Training vs Inference (1 hour)

### Practice Exercises
Run `week9/practice/04_testing_implications.py`.

## Friday: Review (1 hour)

Connect all the concepts: how tokens flow through a model, how temperature affects output, and what this means for testing.

## Week 9 Deliverables

## Saturday-Sunday: Build `llm-concepts-notebook`

**Mini-Project: `llm-concepts-notebook`**

### Why this matters in AI testing?
You cannot test what you do not understand. Before writing a single LLM test, you need a mental model for how these systems generate text, why they are non-deterministic, and what parameters influence their behavior. This notebook becomes your reference guide.

### Learning Focus
- Documenting LLM concepts in your own words
- Creating visual explanations and diagrams
- Connecting each concept to a testing implication
- Building a reference you will use throughout the journey

### Mini-Project Overview
**Two reusable utilities: a token generation simulator and a prompt analyzer.**
```
llm-concepts-notebook/
├── core/
│   ├── simulator.py
│   └── analyzer.py
└── main.py
```
