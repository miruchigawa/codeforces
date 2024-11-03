def is_palindromic(x):
    return str(x) == str(x)[::-1]

def sieve(limit):
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if prime[i]:
            for j in range(i * i, limit + 1, i):
                prime[j] = False
    return prime

def precompute_counts(limit):
    prime = sieve(limit)
    
    prime_count = [0] * (limit + 1)
    palindromic_count = [0] * (limit + 1)
    
    for i in range(1, limit + 1):
        prime_count[i] = prime_count[i - 1] + (1 if prime[i] else 0)
        palindromic_count[i] = palindromic_count[i - 1] + (1 if is_palindromic(i) else 0)
    
    return prime_count, palindromic_count

def find_max_n(p, q, limit=2000000):
    prime_count, palindromic_count = precompute_counts(limit)
    max_n = -1
    
    for n in range(1, limit + 1):
        if palindromic_count[n] > 0 and prime_count[n] * q <= p * palindromic_count[n]:
            max_n = n
    
    return "Palindromic tree is better than splay tree" if max_n == -1 else max_n

p, q = map(int, input().split())
print(find_max_n(p, q))
