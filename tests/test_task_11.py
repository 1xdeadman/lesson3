import collections.abc as abc

import pytest
import random as rnd
import tasks.task_11 as task_11


@pytest.mark.task_11
def test_Child():
    value = rnd.randint(-1000, 1000)
    test_elem = task_11.Child(value)
    assert "common_value" in dir(task_11.Child)
    assert "data" in dir(test_elem)
    assert "test_value" in  dir(test_elem)
    assert "create_zero_class" in dir(test_elem)
    assert "child_data" in dir(test_elem)
    assert "child_data" not in dir(task_11.Child)
    assert type(test_elem.child_data) is dict
    assert test_elem.child_data['key'] == 'value'

    assert test_elem.test_value == value
    assert test_elem.data == "text"

    test_elem2 = task_11.Child("Sad")

    assert "test_value" not in dir(test_elem2)
    assert "data" in dir(test_elem2)

    class TestChild(task_11.Child):
        pass

    test_child_elem = TestChild.create_zero_class()

    assert type(test_child_elem) is TestChild
    assert isinstance(test_child_elem, task_11.Child)
    assert isinstance(test_child_elem, task_11.Parent)

    test_child_elem = task_11.Child.create_zero_class()

    assert type(test_child_elem) is task_11.Child
    assert isinstance(test_child_elem, task_11.Child)
    assert isinstance(test_child_elem, task_11.Parent)