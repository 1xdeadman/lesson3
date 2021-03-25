import pytest
import random as rnd
import tasks.task_12 as task_12
import os


@pytest.mark.task_12
def test_MyException():

    with pytest.raises(task_12.MyException) as ex:
        raise task_12.MyException("lolkekazaza")

    ex = task_12.MyException("text")
    assert "message" in dir(ex)
    assert ex.message == "text"


@pytest.mark.task_12
def test_func():

    def sub_func(param1, param2, param3):
        assert type(param1) is not tuple
        assert param1 == param2
        assert param3 == str(param1) + "!"
        if param1 < 10:
            raise ValueError()
        elif param1 > 20:
            raise TypeError()
        elif param1 == 10:
            raise task_12.MyException("lolkek")
        else:
            raise Exception("lolkek")

    res = task_12.func(sub_func, 10, 10, "10!")
    assert res == "Реализованно"

    res = task_12.func(sub_func, 0, 0, "0!")
    assert res == "ValueError"

    res = task_12.func(sub_func, 220, 220, "220!")
    assert res == 1

    res = task_12.func(sub_func, 15, 15, "15!")
    print(res)
