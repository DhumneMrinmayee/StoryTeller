from fastapi import FastAPI, HTTPException
from Tagline import create_tagline, create_keyword
from typing import List

app = FastAPI()
max_input_length = 5000


@app.get("/Thecking_mistakes")
async def checking_mistakes_api(prompt: str):
    valid_in_len(prompt)
    mistakes = checking_mistakes(prompt)
    return {"snippet": mistakes, "keywords": None}


@app.get("/generate_recommendations")
async def generate_recommendations_api(prompt: str):
    valid_in_len(prompt)
    recommendation = generate_recommendations(level, experience, prompt)
    return {"snippet": None, "keywords": keywords}


@app.get("/Generate_tagline&keywords")
async def create_keywords_api(prompt: str):
    valid_in_len(prompt)
    snippet = create_tagline(prompt)
    keywords = create_keyword(prompt)
    return {"snippet": snippet, "keywords": keywords}


def valid_in_len(prompt: str):
    if len(prompt) >= max_input_length:
        raise HTTPException(status_code=400,
                            detail=f"invalid  input character length.Must be under {max_input_length}"
                            )
    pass

# uvicorn Tagline_fastapi:app --reload
