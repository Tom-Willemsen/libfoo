from libfoo.version import version


def test_version_is_importable():
    assert version is not None
