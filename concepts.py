class Worker():
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn= fn
        self.args=args 
        self.kwargs= kwargs
    def run(self):
           result = self.fn()

def testfun():
    print("my function")

if __name__ == "__main__":
    wrk = Worker(testfun,"dasd",{'one':1})
    wrk.run()