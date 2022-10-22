import time


def timer(runner):

    def wrapped_timer_printer():
        print("####################RUNNING THE ALGORITHM####################")
        tic = time.time()
        runner()
        toc = time.time()
        print("####################### %5.3fs elapsed ##################" %
              (toc - tic))
    return wrapped_timer_printer
