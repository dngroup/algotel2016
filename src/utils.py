import time


class timed(object):
    '''
    decorator used to print execution time and stats on a simulation
    '''

    def __init__(self, f):
        self.f = f
        self.start = time.time()

    def __call__(self, relax_vhg, relax_vcdn, proactive, seed, sla_count, rejected_threshold, iteration_threshold, name,preassign_vhg):
        self.start = time.time()
        res = self.f(relax_vhg, relax_vcdn, proactive, seed, sla_count, rejected_threshold,iteration_threshold,preassign_vhg)
        print(        "%s in %lf for %d run : %lf" % (            name, time.time() - self.start, len(res), (time.time() - self.start) / (1 + len(res))))
        return res
