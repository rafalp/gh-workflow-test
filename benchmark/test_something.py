from dosomething import do_something


def test_benchmark_something(benchmark):
    result = benchmark(do_something)
    assert result
