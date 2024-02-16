#----------------------- Imitating expensive objects ----------------------

from flight_status_redis import FlightStatusTracker
from unittest.mock import Mock
from unittest.mock import patch
import pytest
import datetime

@pytest.fixture
def tracker():
    return FlightStatusTracker()


def test_mock_method(tracker):
    tracker.redis.set = Mock()
    with pytest.raises(ValueError) as ex:
        tracker.change_status("AC101","lost")

    assert ex.value.args[0] == "LOST is not a valid status."
    assert tracker.redis.set.call_count == 0

def test_patch(tracker):
    tracker.redis.set = Mock()
    fake_now = datetime.datetime(2024,2,16)
    with patch("datetime.datetime") as dt:
        dt.now.return_value = fake_now
        tracker.change_status("AC101","on-time")
    dt.now.assert_called_once_with()
    tracker.redis.set.assert_called_once_with(
        "flightno:AC101","2024-02-16T00:00:00 | ON-TIME"
    )