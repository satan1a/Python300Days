class Chain(object):
    """
    无论API怎么变，SDK都可以根据URL实现完全动态的调用
    """
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__