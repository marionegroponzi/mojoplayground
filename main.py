import subprocess
from fastapi import FastAPI, HTTPException
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, magic!"}

@app.get("/zero")
def zero():
    try:
        p = subprocess.Popen(
            ["magic", "run", "mojo", "local/zero.mojo"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        while True:
            output = p.stdout.readline()
            if output == "" and p.poll() is not None:
                raise HTTPException(
                    status_code=500, detail="Failed to produce zero"
                )

            return {"message": f"answer is {output}"}

    except subprocess.SubprocessError as e:
        raise HTTPException(status_code=500, detail="Failed to execute subprocess")

@app.get("/one")
def zero():
    try:
        p = subprocess.Popen(
            ["magic", "run", "bash", "-c", os.path.join("local","zero")],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        while True:
            output = p.stdout.readline()
            if output == "" and p.poll() is not None:
                raise HTTPException(
                    status_code=500, detail="Failed to produce zero"
                )

            return {"message": f"answer is {output}"}

    except subprocess.SubprocessError as e:
        raise HTTPException(status_code=500, detail="Failed to execute subprocess")