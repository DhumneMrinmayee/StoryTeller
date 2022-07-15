from fastapi import FastAPI, HTTPException
from Tagline import create_tagline, create_keyword
from typing import List

app = FastAPI()
max_input_length = 32


@app.get("/Tagline_generator")
async def create_tagline_api(prompt: str):
    valid_in_len(prompt)
    snippet = create_tagline(prompt)
    return {"snippet": snippet, "keywords": None}


@app.get("/Keywords_generator")
async def create_keywords_api(prompt: str):
    valid_in_len(prompt)
    keywords = create_keyword(prompt)
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
