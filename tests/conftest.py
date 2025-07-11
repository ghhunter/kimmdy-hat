import pytest

def pytest_addoption(parser):
    parser.addoption('--gpu',action='store_true',dest="gpu",
                     default=False, help="enable gpu memory release tests")
    
@pytest.fixture
def gpu(request):
    return request.config.getoption("--gpu")