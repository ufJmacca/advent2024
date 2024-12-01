FROM python

WORKDIR /app

COPY . .

ENTRYPOINT [ "bash" ]