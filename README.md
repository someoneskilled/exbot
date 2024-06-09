# exbot

This repository contains code for building a chatbot using a pre-trained model from the Hugging Face Model Hub. The chatbot is capable of generating adult NSFW responses based on prompts provided by the user.

## Overview

The chatbot utilizes the DistilGPT-2 and GPT2 model from the Hugging Face Model Hub to generate responses. It takes user prompts as input and generates corresponding responses using the trained model.

## Requirements

To run the code in this repository, you'll need the following dependencies:

- Python 3
- Jupyter Notebook
- Transformers library from Hugging Face (`transformers`)

You can install the necessary Python packages using the following command:

```bash
pip install transformers
```

## Usage

1. Clone this repository to your local machine.
2. Open the `exbot_distil.ipynb` notebook using Jupyter Notebook.
3. Follow the instructions within the notebook to run the chatbot.
4. Provide prompts to the chatbot and observe the generated responses.

## Fine-tuning a Model

To fine-tune your own model, follow these steps:

1. Prepare your dataset in the required format.
2. Install the Transformers library and other dependencies as mentioned in the requirements.
3. Use the provided code or modify it to fine-tune your model on the dataset.
4. Once fine-tuning is complete, upload your model to the Hugging Face Model Hub for easy access.

## Sample Dataset

The repository includes a sample dataset (`dataset.json`) containing prompts and corresponding responses for testing the chatbot.

## Hugging Face Model

The chatbot uses a pre-trained DistilGPT-2 model from the Hugging Face Model Hub. You can find the model repository [here](https://huggingface.co/someoneskilled/fine-tuned-distilgpt2-exbot).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project utilizes the Transformers library developed by Hugging Face.
- Special thanks to the Hugging Face community for their contributions and support.
