import pytest
import random as rnd
import tasks.task_9 as task_9


@pytest.mark.task_9
def test_constructor():
    test_elem1 = task_9.YourClass()
    test_elem2 = task_9.YourClass()
    assert 'data' in dir(test_elem1)
    assert type(test_elem1.data) is list
    assert len(test_elem1.data) == 0
    assert id(test_elem1.data) != id(test_elem2.data)


@pytest.mark.task_9
def test_concat():

    for step in range(10):
        test_elem = task_9.YourClass()
        text = ""
        for i in range(100):
            new_value = rnd.randint(1, 10000)
            text += f"{new_value} "
            test_elem.data.append(new_value)

        assert test_elem.concat() == text[:-1]
