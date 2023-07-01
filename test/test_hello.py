import pytest
from src.service.print_hello import print_hello 



def test_mytest():
    assert 'hello world' == print_hello()
    assert 1==2
    

# def f():
#     raise SystemExit(1)


# def test_mytest():
#     with pytest.raises(SystemExit):
#         f()