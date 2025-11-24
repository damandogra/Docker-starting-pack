from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    poem = 'Two roads diverged in a yellow wood, \n And sorry I could not travel both \nAnd be one traveler, long I stood \nAnd looked down one as far as I could \nTo where it bent in the undergrowth; \nThen took the other, as just as fair, \nAnd having perhaps the better claim, \nBecause it was grassy and wanted wear; \nThough as for that the passing there \nHad worn them really about the same, \nAnd both that morning equally lay \nIn leaves no step had trodden black. \nOh, I kept the first for another day! \nYet knowing how way leads on to way, \nI doubted if I should ever come back. \nI shall be telling this with a sigh \nSomewhere ages and ages hence: \nTwo roads diverged in a wood, and I— \nI took the one less traveled by, \nAnd that has made all the difference.'
    lines = poem.split('\n')
    return {
        'The road not taken by Robert Frost': lines,
        "env": os.getenv("ENV", "local")
    }