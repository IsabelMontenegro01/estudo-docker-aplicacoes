# Atividade: monitor de sensores com Docker Compose e 5C

## Contexto

Uma equipe de manutenção precisa consultar o estado de sensores industriais por uma página web. A aplicação já possui:

- uma API Flask em `api/`, que responde em `GET /status`;
- um frontend Nginx em `frontend/`, que encaminha `/api/` para o serviço interno chamado `api`.

Sua equipe deve criar o arquivo `compose.yaml` para executar a aplicação como dois serviços.

## Produto esperado

O projeto deve subir com:

```bash
docker compose up --build -d
```

O navegador deve acessar o frontend em `http://localhost:8081`. A API deve permanecer disponível apenas para o frontend na rede interna do Compose.

## Critérios de validação

1. O `compose.yaml` declara os serviços `frontend` e `api`.
2. Cada serviço usa o contexto de build correto.
3. Somente o frontend publica uma porta para o computador hospedeiro.
4. A página em `http://localhost:8081` mostra o estado dos sensores.
5. `docker compose ps` e `docker compose logs` oferecem evidências para explicar o resultado.

## Registro pelo 5C

Preencha [registro-5c.md](registro-5c.md) durante a atividade. A equipe pode usar IA para esclarecer uma dúvida técnica, mas deve registrar a hipótese, confrontar a orientação com a documentação ou um teste e explicar a decisão tomada.

## Comandos úteis

```bash
docker compose config
docker compose up --build -d
docker compose ps
docker compose logs -f
docker compose down
```

Não há solução do Compose nesta pasta. A evidência da equipe é o arquivo criado, a execução demonstrável e o registro 5C.
