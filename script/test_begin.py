import pytest

from utils import DriverUtils

@pytest.mark.run(order=0)
class TestBegin:
    def test_begin(self):
        DriverUtils.change_key(False)