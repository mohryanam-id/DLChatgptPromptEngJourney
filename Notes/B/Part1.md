# Write Clear and Specific Instruction

[Back](README.md) | [Next](Part1.md)

This will guide the model towards the desired output and reduce the chance that you get irrelevant or incorrect responses. Don't confuse writing a clear prompt with writing a short prompt, because in many cases, longer prompts actually provide more clarity and context for the model, which can actually lead to more detailed and relevant outputs.

## [Use delimiters](../../Codes/principle1_1.py)

Use delimiters to clearly indicate distinct parts of the input.

- Triple quotes: """
- Triple backticks: ```
- Triple dashes: ---
- Angle brackets: < >,
- XML tags: `<tag> </tag>`

Delimiters can be kind of any clear punctuation that separates specific pieces of text from the rest of the prompt.

Using delimiters is also a helpful technique to try and avoid prompt injections.

What a prompt injection is, is if a user is allowed to add some input into your prompt, they might give kind of conflicting instructions to the model that might kind of make it follow the user's instructions rather than doing what you wanted it to do.

```python
'<content> ... </content>'
```

### Example 1

- Using delimiters to specify text for summarization. A paragraph is given, and the goal is to summarize it.

- The prompt instructs the model to summarize the text enclosed by triple backticks into a single sentence. The response is obtained using a helper function and then printed.

- By running the code, a sentence output is received, indicating successful summarization based on the specified delimiters. Delimiters can be any clear punctuation that separates specific text portions from the rest of the prompt.

- They help clarify the intended sections for the model and can prevent prompt injections, where conflicting user instructions may mislead the model. Delimiters ensure that the model focuses on summarizing the designated text rather than following external instructions.

- Prompt result:

```txt
To guide a model towards the desired output and reduce the chances of irrelevant or incorrect responses, it is important to provide clear and specific instructions, which may require longer prompts for more clarity and context.
```

## [Ask for Structured Output](../../Codes/principle1_2.py)

To make parsing the model outputs easier, it can be helpful to ask for a structured output like HTML or JSON.

```python
# sample additional information
'Provide them in JSON format with the following keys: book_id, title, author, genre.'
```

### Example 2

- The prompt instructs the model to generate a list of three fictitious book titles, along with their authors and genres.

- The desired output format is JSON, with keys for book ID, title, author, and genre.

- The example demonstrates the resulting JSON structure, which can be easily read into a dictionary or a list in Python.

- This format allows for convenient data processing and manipulation in Python.

- Prompt result:

```json
[
  {
    "book_id": 1,
    "title": "The Lost City of Zorath",
    "author": "Aria Blackwood",
    "genre": "Fantasy"
  },
  {
    "book_id": 2,
    "title": "The Last Survivors",
    "author": "Ethan Stone",
    "genre": "Science Fiction"
  },
  {
    "book_id": 3,
    "title": "The Secret of the Haunted Mansion",
    "author": "Lila Rose",
    "genre": "Mystery"
  }
]
```

## [Check Whether Conditions are Satisfied](../../Codes/principle1_3.py)

If the task makes assumptions that aren't necessarily satisfied, then we can tell the model to check these assumptions first. And then if they're not satisfied, indicate this and kind of stop short of a full task completion attempt. You might also consider potential edge cases and how the model should handle them to avoid unexpected errors or result.

```python
'If the text does not contain a sequence of instructions, then simply write "No steps provided."'
```

### Example 3

- The importance of checking assumptions and handling potential edge cases when interacting with the model. It suggests instructing the model to verify assumptions before proceeding with a task and stopping if the assumptions are not met.

- Considering edge cases helps avoid unexpected errors or outcomes. An example is presented where a prompt instructs the model to rewrite instructions from a paragraph describing the steps to make a cup of tea.

- The model successfully extracts the instructions when provided with the appropriate text. Another example is given using a paragraph about a sunny day without any instructions.

- Running the same prompt on this text correctly results in the model recognizing the absence of instructions and responding with "no steps provided."

- First prompt result:

```txt
Completion for Text 1:
Step 1 - Get some water boiling.
Step 2 - Grab a cup and put a tea bag in it.
Step 3 - Once the water is hot enough, pour it over the tea bag.
Step 4 - Let it sit for a bit so the tea can steep.
Step 5 - After a few minutes, take out the tea bag.
Step 6 - Add some sugar or milk to taste.
Step 7 - Enjoy your delicious cup of tea!
```

- Second prompt result:

```txt
Completion for Text 2:
No steps provided.
```

## ["Few-shot" Prompting](../../Codes/principle1_4.py)

This is just providing examples of successful executions of the task you want performed before asking the model to do the actual task you want it to do.

### Example 4

- An example is presented where the prompt instructs the model to answer in a consistent style.

- A conversation between a child and a grandparent serves as the example, with the grandparent providing metaphors in response to the child's requests.

- By instructing the model to maintain a consistent tone, it can generate a response in a similar style when given a new instruction.

- Prompt result:

```txt
<grandparent>: Resilience is like a tree that bends with the wind but never breaks. It is the ability to bounce back from adversity and keep moving forward, even when things get tough. Just like a tree needs strong roots to weather a storm, we need to cultivate inner strength and perseverance to overcome life's challenges.
```

[Back to Top](#write-clear-and-specific-instruction)
