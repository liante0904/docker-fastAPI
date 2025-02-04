from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()

@app.on_event("startup")
async def warm_up():
    for attempt in range(5):  # 최대 5번 재시도
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get("http://localhost:8000/")
                if response.status_code == 200:
                    print("Warm-up successful!")
                    break
        except httpx.RequestError:
            print(f"Warm-up attempt {attempt + 1} failed. Retrying...")
            await asyncio.sleep(2)  # 2초 대기

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/reports/global/")
def report_global():
    return {"report": "Global Report"}
