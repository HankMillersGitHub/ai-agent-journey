import random

import pytest
import random


def test_4():
    pass
def test_2():
    pass

@pytest.mark.dt
def test_rerun_failures():
    n = random.randint(1,10)
    assert n >= 5
