class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, number):
        if self.next_handler:
            return self.next_handler.handle(number)
        return "No consumido"

class PrimeHandler(Handler):
    def handle(self, number):
        if self.is_prime(number):
            print(f"Consumido por PrimeHandler: {number}")
            return f"Consumido por PrimeHandler: {number}"
        else:
            return super().handle(number)

    def is_prime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

class EvenHandler(Handler):
    def handle(self, number):
        if number % 2 == 0:
            print(f"Consumido por EvenHandler: {number}")
            return f"Consumido por EvenHandler: {number}"
        else:
            return super().handle(number)

# Cadena de responsabilidad
handler_chain = PrimeHandler(EvenHandler())

# Test
for i in range(1, 101):
    handler_chain.handle(i)