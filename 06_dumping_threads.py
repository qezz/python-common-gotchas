import sys
import traceback

def dump_threads():
    for thread_id in sys._current_frames():
        print("Thread", thread_id, "{")
        frame = sys._current_frames()[thread_id]
        # print(str(traceback.format_stack(frame)))
        # pprint(traceback.format_stack(frame))
        for line_ in traceback.format_stack(frame):
            print(">-", line_, "-<")
        print("}")
