FROM python:3.14-rc-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /devsearch
COPY requirements.txt /devsearch

RUN pip install --upgrade pip
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    harfbuzz-dev \
    fribidi-dev
RUN pip install -r requirements.txt
RUN apk del .build-deps
COPY . /devsearch

EXPOSE 8000
