n = 15 * 10 ** 6
b = [True for _ in range(n + 1)]
i = 2
while i ** 2 <= n:
    if b[i]:
        j = i ** 2
        while j <= n:
            b[j] = False
            j += i
    i += 1
primes = [x for x in range(2, n + 1) if b[x]]


class Primes:
    @staticmethod
    def stream():
        p = iter(primes)
        while True:
            try:
                yield next(p)
            except StopIteration:
                return


def verify(from_n):
    stream = Primes.stream()
    for _ in range(from_n): next(stream)
    for i in range(10): print(next(stream))

verify(1 * 10 ** 6)
