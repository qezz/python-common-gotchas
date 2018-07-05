import sys
from pprint import pprint

def print_frame_info(frame):
    print ('module: %s' % frame.f_globals.get('__name__'))
    print ('filename: %s' % frame.f_code.co_filename)
    print ('current line: %d' % frame.f_lineno)
    # loc = dict((k, v) for k, v in frame.f_locals # .iteritems()
    #            if not k.startswith('__'))
    # print ('local variables: %s' % loc)
    print("frame locals:")
    pprint(frame.f_locals)

# print_frame_info(sys._getframe())
