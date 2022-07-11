import os
from typing import List

import openai
import argparse  # Python Command-Line Parsing Libraries
import re

max_input_length = 100


def main():
    # print("Welcome to Tagline")

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    arguments = parser.parse_args()
    user_prompt = arguments.input

    print("user_prompt :", user_prompt)
    if valid_len(user_prompt):
        create_tagline(user_prompt)
        create_keyword(user_prompt)
    else:
        raise ValueError(
            f"Prompt exceed the character limit. It must be under {max_input_length}.submitted input is{user_prompt}")


# function for deciding maximum valid input character length
def valid_len(snippet: str) -> bool:
    return len(snippet) <= max_input_length


# Load your API key from an environment variable or secret management service



def create_tagline(snippet: str) -> str:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f" Creative a branding for the Advertisement  of a product {snippet}: "
    response = openai.Completion.create(model="text-curie-001",
                                        prompt=prompt,
                                        temperature=0, max_tokens=250)

    tagline_text: str = response["choices"][0]["text"]  # extract only output text
    tagline_text = tagline_text.strip()  # removing white space within output text
    end_char = tagline_text[-1]
    if end_char not in {".", "!", "?"}:  # ending of the output text:  Added "..." for truncate the text
        tagline_text += "...!"

    print("Result:", tagline_text)
    return tagline_text


def create_keyword(words: str) -> List[str]:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt = f"Creative keywords network for the product {words}: "
    print(prompt)

    response = openai.Completion.create(model="text-curie-001",
                                        prompt=prompt,
                                        temperature=0, max_tokens=32)
    # print(response)

    keywords: str = response["choices"][0]["text"]  # extract only output text
    keywords = keywords.strip()
    word_array = re.split(",| \n |;|- ", keywords)
    word_array = [a.lower().split() for a in word_array]
    word_array = [a for a in word_array if len(a) > 0]

    print("Keywords:", word_array)
    return word_array


if __name__ == "__main__":
    main()

"""git add .
git commit -m "add Tagline.py"
git remote add origin https://github.com/DhumneMrinmayee/StoryTeller/.git/Tagline.py
git push origin master or git push -f  Tagline.py"""
