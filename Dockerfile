FROM python:3.7.4 as base

FROM base as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt /requirements.txt

RUN pip install --upgrade pip

RUN apt-get install libssl-dev libffi-dev

RUN pip install --install-option="--prefix=/install" -r /requirements.txt

FROM base

COPY --from=builder /install /usr/local

COPY . /app

WORKDIR /app

EXPOSE 5000

RUN python

CMD ["gunicorn", "-b :5000", "-w 3", "--access-logfile", "-", "--error-logfile", "-", "run:app"]
