import os
import openai
import argparse
import re

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--level", "-l", type=str, required=True, help='Level of expertise: Beginner, Intermediate, '
                                                                       'Expert')
    parser.add_argument("--experience", "-e", type=int, required=True, help='Experience years in the field')
    parser.add_argument("--input", "-i", type=str, required=True, help='Paste your snippet')
    args = parser.parse_args()

    print(args.level)
    print(args.experience)
    print(args.input)
    result_mistakes = checking_mistakes(args.input)
    print('\n \t English grammar and spelling mistakes\t \n',result_mistakes)
    results = generate_recommendations(args.level, args.experience, args.input)
    print('\n\n \tThis feedback will be open-ended and include examples or suggestions.\t', '\n\n\n',results)


def checking_mistakes(prompt : str) -> list[str]:
    openai.api_key = os.getenv("OPENAI_API_KEY")  # load API key form openai

    enrich_prompt = f" Proofreading of {prompt}, comment on correctness. List all grammar mistakes in the {prompt}"


    mistakes_found = openai.Completion.create(model="text-davinci-002", prompt=enrich_prompt, temperature=0.7, max_tokens= 800)
    # extract output text
    mistakes_found = mistakes_found['choices'][0]['text']
    mistakes_found = mistakes_found.strip()  # strip white space

    return mistakes_found


def generate_recommendations(level, experience, prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")  # load API key form openai
    # level = "expert"
    # experience = 20
    # story = open("/stories/")
    enrich_prompt = f" I am a creative writing{level}. I have been a professional editor for {experience} years. I am going to " \
                    f"provide you following short paragraph and you will give " \
                    f"I am going to read the following short story and provide you critical feedback to improve your " \
                    f"prose. I will hold you to the highest literary standards, and my feedback will be open-ended " \
                    f"and include examples or suggestions. I will also commend you where you did well. {prompt}: " \
                    f"Story ends. \n I will now give you one or two paragraphs of critical feedback to improve your " \
                    f"prose and articulate the style. I will use compliment sandwich method for feedback"\

    response = openai.Completion.create(model="text-davinci-002", prompt=enrich_prompt, temperature=0.7, max_tokens=400)
    # extract output text
    response = response['choices'][0]['text']
    response = response.strip()  # strip white space
    # Add space to truncated statements
    last_char = response[-1]

    if last_char not in {".", "!", "?"}:
        response += " "
    return response




if __name__ == "__main__":
    main()
