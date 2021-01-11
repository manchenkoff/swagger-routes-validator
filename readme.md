# Swagger routes validator

A specific helper to check API routes coverage with Swagger.

## How to use

This application is provided only by Docker image and can be used as following example

```bash
$ docker run -i \
    -v $(PWD)/data:/var/data \
    -e CONFIG=/var/data/config.yml \
    --name swagger-routes-validator --rm \
    manchenkoff/swagger-routes-validator:latest
```

Config example

```yaml
swagger: tests/data/example/swagger-doc/swagger.yml

routes:
  default:
    path: tests/data/example/routing/v1.yml
  with_prefix:
    path: tests/data/example/routing/v2.yml
    prefix: /v2
```

### Environments variables

- **CONFIG**: path to config file