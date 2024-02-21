#-----------------------   Queues ------------------------

def search(paths,query_q, result_q):
    lines = []
    for path in paths:
        lines.extend(l for l in path.open())

    query = query_q.get()
    while query:
        result_q.put([l for l in lines if query in l])
        query = query_q.get()


if __name__ == "__main__":
    from multiprocessing import Process, Queue, cpu_count
    from path import Path

    cpus = cpu_count()
    pathnames = [f for f in Path(".").iterdir() if f.isfile()]
    paths = [pathnames[i::cpus] for i in range(cpus)]
    query_queues = [Queue() for _ in range(cpus)]
    result_queue = Queue()
    search_procs = [
        Process(target=search,args=(p,q,result_queue))
        for p, q in zip(paths,query_queues)
    ]

    for proc in search_procs:
        proc.start()

    for q in query_queues:
        q.put("def")
        q.put(None)

    for _ in range(cpus):
        for match in result_queue.get():
            print(match)

    for proc in search_procs:
        proc.join()