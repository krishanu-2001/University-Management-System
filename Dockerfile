FROM alpine:latest

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add py3-pip \
    && apk add --no-cache mariadb-dev

WORKDIR /univ

COPY . /univ

RUN pip3 install 'pip==20.3.3'
RUN pip3 install --user -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]