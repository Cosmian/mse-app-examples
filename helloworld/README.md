# Helloworld

Basic example of an mse application working with a self-signed certificate on a fully zero trust environment and containing:
- A simple helloworld flask application
- The mse app config file
- Python tests

## Deploy your application

```console
$ mse deploy 
```

Your application is now ready to be used

## Test it

```console
$ TEST_REMOTE_URL="https://$APP_DOMAIN_NAME" pytest
```

## Use it 

You can get the certificate and check it using:

```console
$ mse verify "$APP_DOMAIN_NAME"
```

You can now query the microservice:

```sh
$ curl https://$APP_DOMAIN_NAME/ --cacert cert.pem
```