from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pix2pix import image_edit
from pydantic import BaseModel
from complete import generate_stable_image

class data(BaseModel):
    path: str
    prompt_inp: str

    class Config:
        orm_mode = True
class new_d(BaseModel):
    prompt_inp: str

    class Config:
        orm_mode = True


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/modify")
def pix2pix(inp: data):
    return image_edit(inp.path, inp.prompt_inp)

@app.post("/new")
def new(inp:new_d):
    return generate_stable_image(inp.prompt_inp)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000, reload=True)
