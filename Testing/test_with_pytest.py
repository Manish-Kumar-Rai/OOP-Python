#------------------- Fixtures--------------------
import pytest
from stats import StatsList

@pytest.fixture
def valid_stats():
    return StatsList([1,2,2,3,3,4])

def test_mean(valid_stats):
    assert valid_stats.mean() == 2.5