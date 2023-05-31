# [Halucination](../../Codes/halucination.py)

[Back](Part2.md)

Although the model has been exposed to a vast amount of information during training, it does not have perfect knowledge of all topics. As a result, it may generate answers about obscure subjects and produce fabricated ideas that sound plausible but are not true, which are referred to as hallucinations.

The model can confabulate a description of a fictitious product when given a prompt about it. It emphasizes the danger of such hallucinations because they can sound realistic. The author advises using techniques outlined in the notebook to avoid these issues when building applications. They acknowledge that hallucinations are a known weakness of the models and efforts are being made to combat them.

To reduce hallucinations, one suggested tactic is to ask the model to find relevant quotes from a text and use them to answer questions. This way, the answer can be traced back to the source document, which helps in reducing hallucinations. The content concludes by mentioning that the guidelines for prompting are complete.

## Example

_Tell me about AeroGlide Ultra Slim Smart Toothbrush by Boy_. So if we run this, the model is going to give us a pretty realistic sounding description of a fictitious product. And the reason that this can be kind of dangerous is that this actually sounds pretty realistic.

- prompt result:

```txt
The AeroGlide UltraSlim Smart Toothbrush by Boie is a high-tech toothbrush that uses advanced sonic technology to provide a deep and thorough clean. It features a slim and sleek design that makes it easy to hold and maneuver, and it comes with a range of smart features that help you optimize your brushing routine.

One of the key features of the AeroGlide UltraSlim Smart Toothbrush is its advanced sonic technology, which uses high-frequency vibrations to break up plaque and bacteria on your teeth and gums. This technology is highly effective at removing even the toughest stains and buildup, leaving your teeth feeling clean and refreshed.

In addition to its sonic technology, the AeroGlide UltraSlim Smart Toothbrush also comes with a range of smart features that help you optimize your brushing routine. These include a built-in timer that ensures you brush for the recommended two minutes, as well as a pressure sensor that alerts you if you're brushing too hard.

Overall, the AeroGlide UltraSlim Smart Toothbrush by Boie is a highly advanced and effective toothbrush that is perfect for anyone looking to take their oral hygiene to the next level. With its advanced sonic technology and smart features, it provides a deep and thorough clean that leaves your teeth feeling fresh and healthy.
```

[Back to Top](#halucination)
