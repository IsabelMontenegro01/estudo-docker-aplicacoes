FROM golang:1.23-alpine AS build

WORKDIR /app

COPY go.mod ./
COPY main.go ./

RUN go build -o calculadora .

FROM alpine:3.20

WORKDIR /app

COPY --from=build /app/calculadora .

EXPOSE 5000

CMD ["./calculadora"]