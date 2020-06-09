import subprocess as sub
import threading
import time

mytime=time.strftime("%Y-%m-%d-%H:%M:%S")
fname ="/file path/"+mytime+".txt"
class RunCmd(threading.Thread):
    def __init__(self, cmd, timeout):
        threading.Thread.__init__(self)
        self.cmd = cmd
        self.timeout = timeout

    def run(self):
        #self.p = sub.Popen(self.cmd)
        #mytime=time.strftime("%Y-%m-%d-%H:%M:%S")
        #fname="/file path/"+ mytime + ".txt";
        #with open("/home/www/tweepy/output/"+ mytime + ".txt", "w+") as output:
        with open(fname, "w+") as output:
                self.p = sub.Popen(self.cmd,stdout=output)
        self.p.wait()

    def Run(self):
        self.start()
        self.join(self.timeout)

        if self.is_alive():
            self.p.terminate()      #use self.p.kill() if process needs a kill -9
            self.join()

RunCmd(["python", "/home/tweepy/all_twitter_streaming.py"],7210).Run()
sub.call(['python3','/home/tweepy/data.py',fname])
sub.call(['gzip',fname])

