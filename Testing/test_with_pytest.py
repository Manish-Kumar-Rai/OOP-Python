#------------------- Fixtures--------------------
import pytest
from stats import StatsList
import os.path, shutil, tempfile

# @pytest.fixture
# def valid_stats():
#     return StatsList([1,2,2,3,3,4])

# def test_mean(valid_stats):
#     assert valid_stats.mean() == 2.5

# def test_median(valid_stats):
#     assert valid_stats.median() == 2.5
#     valid_stats.append(4)
#     assert valid_stats.median() == 3

# def test_mode(valid_stats):
#     assert valid_stats.mode() == [2,3]
#     valid_stats.remove(3)
#     assert valid_stats.mode() == [2]


# @pytest.fixture
# def temp_dir(request):
#     dir = tempfile.mkdtemp()
#     print(dir)
#     yield dir
#     shutil.rmtree(dir)

# def test_osfiles(temp_dir):
#     os.mkdir(os.path.join(temp_dir,"a"))
#     os.mkdir(os.path.join(temp_dir,"b"))
#     dir_contents = os.listdir(temp_dir)
#     assert len(dir_contents) == 2
#     assert "a" in dir_contents
#     assert "b" in dir_contents

#--------------- scope of a fixture ---------------
# import socket
# import subprocess
# import time

# @pytest.fixture(scope="session")
# def echoserver():
#     print("Loading Server....")
#     p = subprocess.Popen(["python3","server.py"])
#     time.sleep(1)
#     yield p
#     p.terminate()

# @pytest.fixture
# def clientsocket(request):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect(("localhost",1028))
#     yield s
#     s.close()


# def test_echo1(echoserver,clientsocket):
#     clientsocket.send(b"abc")
#     assert clientsocket.recv(3) == b"abc"

# def test_echo(echoserver,clientsocket):
#     clientsocket.send(b"def")
#     assert clientsocket.recv(3) == b"def"


# ------ Skipping test with pytest------------
import sys

# def test_simple_skip():
#     if sys.platform != "fakeos":
#         pytest.skip("Test works only on fakeOS")
#     fakeos.do_something_fake()
#     assert fakeos.did_not_happen

# @pytest.mark.skipif("sys.version_info <= (3,0)")
# def test_python3():
#     assert b"hello".decode() == "hello"

name= "manishrai"

@pytest.mark.xfail("name == 'manish'")
def test_fails():
    assert 3 == 3