from pathlib import Path

import pytest
from pandas import read_csv


def add(a,b):
    return a + b
# 基于当前文件定位，和运行目录无关
DATA_FILE = Path(__file__).parent / "data.csv"
def load_cases():
    """读取 CSV 并转成 [(a, b, c), ...] 形式的参数列表"""
    df = read_csv(DATA_FILE)  # 若 csv 无表头，加 header=None
    return list(df.itertuples(index=False, name=None))
class TestAdd:
    # @pytest.mark.api
    # def test_int(self):
    #     res1 = add(1, 2)
    #     assert res1 == 3
    # # 预期失败，但是该用例实际会正常运行
    # @pytest.mark.xfail
    # def test_str(self):
    #     res = add('1','2')
    #     assert res == '12'
    #
    # def test_list(self):
    #     res = add([1],[2,3,4])
    #     assert res == [1,2,3,4]

    @pytest.mark.ddt
    @pytest.mark.parametrize("a,b,c", load_cases())
    class TestAdd:
        def test_ddt(self, a, b, c):
            print(a, b, c)
            res = add(int(a), int(b))
            assert res == c


