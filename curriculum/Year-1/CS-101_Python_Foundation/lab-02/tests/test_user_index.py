def test_user_index_get():
    idx = UserIndexModified()
    idx.add(1, "alice")
    idx.add(2, "bob")

    assert idx.get(1) == {"id": 1, "name": "alice"}
    assert idx.get(999) is None


def test_user_index_benchmark_worst_case():
    """Benchmark avec pire cas (dernier élément) et timeit.

    La version naïve parcourt n éléments ; la version dict en parcourt 1.
    Mesure : moyenne sur 1000 runs, pire cas = dernier élément.
    """
    n = 100_000
    naive = UserIndex()
    optimized = UserIndexModified()

    for i in range(n):
        naive.add(i, f"user_{i}")
        optimized.add(i, f"user_{i}")

    target = n - 1  # pire cas : dernier élément

    naive_time = timeit.timeit(lambda: naive.get(target), number=1000) / 1000
    optimized_time = timeit.timeit(
        lambda: optimized.get(target), number=1000
    ) / 1000

    print(f"\nNaive    : {naive_time * 1e6:.2f} µs")
    print(f"Optimized: {optimized_time * 1e6:.2f} µs")
    print(f"Gain     : {naive_time / optimized_time:.0f}x")

    # Avec target = n-1, le rapport devrait être ~100 000×
    assert optimized_time < naive_time