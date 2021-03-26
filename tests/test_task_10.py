import pytest
import random as rnd
import tasks.task_10 as task_10


@pytest.mark.task_10
def test_TestClass():
    text_data = [
        "asd",
        'azxc',
        'vev',
        'ewgvsd',
        'qer32tf43g'
    ]
    test_elem = task_10.MyTestClass()
    test_elem_tmp = task_10.MyTestClass()

    assert "_MyTestClass__value" in dir(test_elem)
    assert type(test_elem._MyTestClass__value) is int
    assert test_elem._MyTestClass__value == 146

    assert "main_data" in dir(test_elem)
    assert type(test_elem.main_data) is list
    assert len(test_elem.main_data) == 0
    assert id(test_elem.main_data) == id(test_elem_tmp.main_data)

    del test_elem_tmp

    assert "add" in dir(test_elem)

    assert "Value" in dir(test_elem)
    assert test_elem.Value == 146
    value = rnd.randint(1, 100)
    test_elem.Value = value
    assert test_elem.Value == value
    assert test_elem._MyTestClass__value == value
    test_elem.Value = 0
    assert test_elem.Value == 0
    assert test_elem._MyTestClass__value == 0
    with pytest.raises(ValueError) as ex:
        tmp = rnd.sample(["sad", True, 3.3, b'asd', list(), dict(), tuple(), set()], 1)[0]
        test_elem.Value = tmp
        test_elem.Value = rnd.randint(-1, -100)

