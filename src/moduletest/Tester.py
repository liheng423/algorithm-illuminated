import time


def timer(runner):

    def wrapped_timer_printer():
        print("####################RUNNING THE ALGORITHM####################")
        tic = time.time()
        result = runner()
        toc = time.time()
        print("####################### %5.3fs elapsed ##################" %
              (toc - tic))
        return result

    return wrapped_timer_printer
