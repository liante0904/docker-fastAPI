from fastapi import FastAPI
import httpx

app = FastAPI()

@app.on_event("startup")
async def warm_up():
    async with httpx.AsyncClient() as client:
        # 주요 라우트에 사전 요청
        await client.get("http://localhost:8000/")
        await client.get("http://localhost:8000/reports/global/")

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/reports/global/")
def report_global():
    return {"report": "Global Report"}
