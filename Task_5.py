def ascii(a, b, n=1):
    if (b+1) == a:
        return chr(b)
    print(f'{a} - {chr(a)}', end='\n' if n % 10 == 0 else ' ')
    return ascii(a + 1, b, n + 1)


ascii(32, 127)