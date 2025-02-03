# FastAPI 기본 이미지 설정
FROM python:3.10-slim

# 필요한 패키지 설치
RUN apt-get update && apt-get install -y tzdata && \
    rm -rf /var/lib/apt/lists/*

# 타임존 설정
ENV TZ=Asia/Seoul

# 작업 디렉터리 설정
WORKDIR /app

# FastAPI 설치
COPY ./app /app
RUN pip install fastapi uvicorn

EXPOSE 8000

# FastAPI 서버 실행
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
