import pytest
from src.sub import sub_func


@pytest.mark.parametrize(
    ["text", "expected"],  # 変数名をリストで指定
    [
        pytest.param(
            "test1", "sub_func: test1", id="test1"  # 上で指定した順番で変数を指定  # テストケースの名前を指定
        ),
        pytest.param("test2", "sub_func: test2", id="test2"),
    ],
)
def test_sub_func(text: str, expected: str) -> None:
    """sub_funcのテスト
    parametrizeを使って、1つのロジックで複数のテストケースを定義できる
    """
    assert sub_func(text) == expected
