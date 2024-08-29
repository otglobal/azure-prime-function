import azure.functions as func
import logging

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(count):
    primes = []
    num = 2
    while len(primes) < count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    count = req.params.get('count')
    if not count:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            count = req_body.get('count')

    if count:
        try:
            count = int(count)
            if count <= 0:
                return func.HttpResponse(
                    "Please provide a positive integer for 'count'.",
                    status_code=400
                )
            primes = generate_primes(count)
            return func.HttpResponse(f"The first {count} prime numbers are: {primes}")
        except ValueError:
            return func.HttpResponse(
                "Please provide a valid integer for 'count'.",
                status_code=400
            )
    else:
        return func.HttpResponse(
             "Please pass a 'count' parameter in the query string or in the request body.",
             status_code=400
        )