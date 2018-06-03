# Airports and Trips

A simple microservices application demonstrated with [Nameko](https://github.com/nameko/nameko)

## Pre-requisites

You will need [docker-compose](https://docs.docker.com/compose/install/) and [docker](https://docs.docker.com/) installed in order to run the application. Refer to the relevant documentation for each.

Also, you will need to have [virtualenv](https://virtualenv.pypa.io/en/latest/) or [pipenv](https://github.com/pypa/pipenv) installed.

## Running

Running the application:

``` bash
docker-compose up
```

Test the running application with:

```bash
$ curl -i -d "{\"airport\": \"first_airport\"}" localhost:8000/airport
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 32
Date: Sun, 27 May 2018 05:05:53 GMT

f2bddf0e506145f6ba0c28c247c54629
```

Query the newly created airport

```bash
$ curl localhost:8000/airport/f2bddf0e506145f6ba0c28c247c54629
{"airport": "first_airport"}
```

Great, now let’s add another airport:

```bash
$ curl -i -d "{\"airport\": \"second_airport\"}" localhost:8000/airport
HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 32
Date: Sun, 27 May 2018 05:06:00 GMT

565000adcc774cfda8ca3a806baec6b5
```

Now we got two airports, That’s enough to form a trip. Let’s create a trip now:

```bash
$ curl -i -d "{\"airport_from\": \"f2bddf0e506145f6ba0c28c247c54629\", \"airport_to\": \"565000adcc774cfda8ca3a806baec6b5\"}" localhost:8000/trip

HTTP/1.1 200 OK
Content-Type: text/plain; charset=utf-8
Content-Length: 32
Date: Sun, 27 May 2018 05:09:10 GMT

34ca60df07bc42e88501178c0b6b95e4
```

As before, that last line represents the trip ID. Let’s check if it was inserted correctly:

```bash
$ curl localhost:8000/trip/34ca60df07bc42e88501178c0b6b95e4
{"trip": "{'from': 'f2bddf0e506145f6ba0c28c247c54629', 'to': '565000adcc774cfda8ca3a806baec6b5'}"}
```

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)