import pytest

from utils import DriverUtils

@pytest.mark.run(order=-1)
class TestEnd:
    def test_end(self):
        DriverUtils.change_key(True)
        # 关闭浏览器
        DriverUtils.quit_driver()