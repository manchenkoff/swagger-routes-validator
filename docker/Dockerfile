# Build fat image to install dependencies
FROM python:3.9-slim as builder

WORKDIR /code

RUN pip install --upgrade pip && pip install pipenv

COPY Pipfile* ./

RUN pipenv lock --requirements > requirements.txt
RUN pip install --user --ignore-installed --upgrade -r requirements.txt

COPY src src
COPY setup* ./

RUN pip install --user .

# Build lightweight application image
FROM python:3.9-slim as application

COPY --from=builder /root/.local /root/.local

ENV PATH=/root/.local/bin:$PATH
ENV SWAGGER=""
ENV ROUTES=""

CMD swagger-routes-validator --swagger $SWAGGER --routes $ROUTES