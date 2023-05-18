# Introduction

## **Two Types of Large Language Models (LLMs)**

### Base LLM

- Predict next word, based on text training data.

EXAMPLE:

If you prompt...

```txt
Once upon a time, there was a unicorn
```

It may predict the next several words...

```txt
that lived in a magicl forest with
all her unicorn friends
```

If you prompt...

```txt
What is the capital of France?
```

Quite possible that the base LLM will complete with...

```txt
What is France's largest city?
What is France's population?
What is the currency of France?
```

### Instruction Tuned LLM

- Tries to follow instructions.

- Fine-tune on instructions and good attempts at following those instructions.

- RLHF: Reinforcement Learning with Human Feedback

- Helpful, Honest, Harmless

EXAMPLE:

If you prompt...

```txt
What is the capital of France?
```

Likely the output something like...

```txt
The capital of France is Paris
```
