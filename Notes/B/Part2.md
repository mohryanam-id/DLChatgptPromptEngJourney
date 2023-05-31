# Give the Model Time to "Think"

[Back](Part1.md) | [Next](Part3.md)

If a model is making reasoning errors by rushing to an incorrect conclusion, you should try reframing the query to request a chain or series of relevant reasoning before the model provides its final answer.

Another way to think about this is that if you give a model a task that's too complex for it to do in a short amount of time or in a small number of words, it may make up a guess which is likely to be incorrect. And you know, this would happen for a person too.

If you ask someone to complete a complex math question without time to work out the answer first, they would also likely make a mistake. So, in these situations, you can instruct the model to think longer about a problem, which means it's spending more computational effort on the task.

## [Specify the Steps Required to Complete a Task. If Needed Ask for Output in a Specified Format](../../Codes/principle2_1.py)

### Example 1

The first prompt specifies the steps, including summarizing a paragraph, translating the summary into French, listing names in the French summary, and outputting a JSON object. The second prompt follows a specific format to ensure the desired output structure. Both prompts are demonstrated with examples, showing the summarized text, French translation, names, and JSON output. The format allows for easier integration with code and provides a standardized structure. The choice of delimiters, either triple backticks or angled brackets, is flexible and based on personal preference.

- First prompt result:

```txt
Completion for prompt 1:
Two siblings, Jack and Jill, go on a quest to fetch water from a well on a hilltop, but misfortune strikes and they both tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.

Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.
Noms: Jack, Jill.

{
  "french_summary": "Deux frères et sœurs, Jack et Jill, partent en quête d'eau d'un puits sur une colline, mais un malheur frappe et ils tombent tous les deux de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.",
  "num_names": 2
}
```

- Second prompt result:

```txt
Completion for prompt 2:
Summary: Jack and Jill go on a quest to fetch water, but misfortune strikes and they tumble down the hill, returning home slightly battered but with their adventurous spirits undimmed.
Translation: Jack et Jill partent en quête d'eau, mais un malheur frappe et ils tombent de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.
Names: Jack, Jill
Output JSON: {"french_summary": "Jack et Jill partent en quête d'eau, mais un malheur frappe et ils tombent de la colline, rentrant chez eux légèrement meurtris mais avec leurs esprits aventureux intacts.", "num_names": 2}
```

## Instruct the Model to Work Out Its Own Solution Before Rushing to a Conclusion

Sometimes we get better results when we kind of explicitly instruct the models to reason out its own solution before coming to a conclusion. And this is kind of the same idea that we were discussing about giving the model time to actually work things out before just kind of saying if an answer is correct or not, in the same way that a person would.

### Example 2

- Two prompts used to determine if a student's math solution is correct or not.

- The first prompt contains a math question and the student's incorrect solution.

- The model mistakenly agrees with the student because it skim-reads the response and assumes it is correct based on one line. To address this, a longer prompt is introduced, instructing the model to work out its own solution first and then compare it to the student's solution. The prompt provides a specific format for the question, student's solution, actual solution, agreement status (yes or no), and student grade (correct or incorrect). Running the second prompt shows that the model correctly calculates the solution and recognizes the student's solution as incorrect. This highlights the importance of allowing the model to perform its own calculations and breaking down tasks into steps for more accurate responses.

- First prompt result:

```txt
The student's solution is correct.
```

- Second prompt result:

```txt
Let x be the size of the installation in square feet.

Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 10x

Total cost: 100x + 250x + 100,000 + 10x = 360x + 100,000

Is the student's solution the same as actual solution just calculated:
No

Student grade:
Incorrect
```

[Back to Top](#give-the-model-time-to-think)
