FROM python:3.9 AS builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Fix libGL.so.1 error when using cv2
RUN apt update &&\
    apt -y --no-install-recommends install gcc ffmpeg libsm6 libxext6

RUN python3 -m pip install --upgrade pip

RUN pip install "uvicorn[standard]" unidecode

COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

FROM builder AS runtime
WORKDIR /app

COPY "./app" .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--workers", "4", "--port", "80"]

