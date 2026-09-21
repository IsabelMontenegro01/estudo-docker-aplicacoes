# Exemplo da aula: Compose com frontend e API

Este exemplo mostra uma aplicação formada por dois serviços:

- `frontend`: servidor Nginx que entrega uma página web na porta `8080`;
- `api`: serviço Flask que responde em uma rede interna na porta `5050`.

O navegador acessa apenas o frontend. O frontend chama a API pelo nome do serviço `api`, sem expor a porta da API no computador hospedeiro.

## Executar

Na pasta deste exemplo, execute:

```bash
docker compose up --build -d
```

Abra <http://localhost:8080> no navegador.

## Observar e validar

```bash
docker compose ps
docker compose logs -f
docker compose config
```

Confirme os pontos abaixo:

1. Os serviços `frontend` e `api` aparecem em execução.
2. A página abre em `http://localhost:8080`.
3. O botão da página recebe uma resposta da API.
4. O log identifica de qual serviço veio cada mensagem.

## Encerrar

```bash
docker compose down
```
