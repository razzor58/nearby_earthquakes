from app.tools import timing


def test_timing_decorator():
    number = 10

    @timing
    def decorated_func(number):
        return number * 2

    result = decorated_func(number)

    assert result == number * 2
