try:
    from website.local_settings import *
except ImportError:
    print "Can't find local settings, use defaults"
    from website.default_settings import *
