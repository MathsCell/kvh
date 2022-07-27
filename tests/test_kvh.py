from pathlib import Path
import pytest
import kvh.kvh as kv

def test_0():
    assert kv.__version__ == '0.1'
    assert kv.kvh_read(str(Path(__file__).parent/"test0.kvh")) == [("key", "value")]

def test_err():
    with pytest.raises(RuntimeError):
        kv.kvh_read("non existing file")
