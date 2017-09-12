from multiprocessing import Process,Pool,Queue
import os
import signal

MAX_PROCESS = 3

q = Queue()

# 子进程要执行的代码
def run_proc(name):
    q.put("Run child process {0} ({1})...".format(name,os.getpid()))
    
def print_q(q_obj):
    print("print process start...")
    while True:
        if not q_obj.empty():
            print(q.get())

if __name__ == "__main__":
    # 父进程id
    print("Parent process {0}.".format(os.getpid()))
    print_process = Process(target=print_q,args=(q,))
    print_process.start()
    
    p = Pool(processes=MAX_PROCESS)
    print("Child process will start.")
    for i in range(MAX_PROCESS*10):
        p.apply_async(run_proc,args=("test",))
    p.close()
    p.join()
    print("Child process end.")
    os.kill(print_process.pid,signal.SIGKILL)