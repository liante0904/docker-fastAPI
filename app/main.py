from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/reports/global/")
def report_global():
    return {"report": "Global Report"}
