from fastapi import FastAPI, HTTPException
from user_interface import checking_mistakes, generate_feedback, validate_length
from typing import List

app = FastAPI()
Max_input_len = 6000


@app.get("/Generate feedback")
async def generate_feedback_api(level, experience, prompt):
    valid_in_len(prompt)
    results = generate_feedback(level, experience, prompt)
    return {"Errors": None, "Feedback": results}

@app.get("/Checking for mistakes")
async def checking_mistakes_api(prompt: str):
    valid_in_len(prompt)
    mistakes = checking_mistakes(prompt)
    return {"Errors": mistakes, "Feedback":None }

@app.get("/Check for the errors and return a feedback")
async def generate_feedback_api(level, experience, prompt):
    valid_in_len(prompt)
    mistakes = checking_mistakes(prompt)
    results = generate_feedback(level, experience, prompt)
    return {"Errors": mistakes, "Feedback": results}


def valid_in_len(prompt: str):
    if len(prompt) >= Max_input_len:
        raise HTTPException(status_code=400,
                            detail=f"invalid  input character length.Must be under {Max_input_len}"
                            )
    pass


# uvicorn  user_interface_api:app --reload