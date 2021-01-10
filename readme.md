# Swagger routes validator

A specific helper to check API routes coverage with Swagger.

## How to use

This application is provided only by Docker image and can be used as following example

```bash
$ docker run \
    -v $(PWD)/data:/var/data \
    -e SWAGGER=/var/data/swagger.yml \
    -e ROUTES=/var/data/routes1.yml,/var/data/routes2.yml \
    --name swagger-routes-validator --rm \
    manchenkoff/swagger-routes-validator:latest
```

### Environments variables

- **SWAGGER**: path or URI to OpenAPI 3 file (Swagger.yml)
- **ROUTES**: path to YAML routes files (separated by a comma)