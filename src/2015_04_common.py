def solve(secret_key, n):
    from hashlib import md5
    from itertools import count

    for i in count(1):
        if md5(bytes(f"{secret_key}{i}", encoding="utf-8")).hexdigest()[:n] == n * "0":
            return i
