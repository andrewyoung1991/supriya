from supriya import servertools


def test_Server_boot_01():

    server = servertools.Server(port=57757)
    for i in range(4):
        assert not server.is_running
        server.boot()
        assert server.is_running
        server.quit()
    assert not server.is_running