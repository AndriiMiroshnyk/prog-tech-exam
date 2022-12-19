FROM alpine
RUN apk add --update python3
COPY . /app
WORKDIR /app
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]