import asyncio, async_timeout, logging

class Node:
    def __init__(self, name, func, timeout=30, retries=1):
        self.name, self.func = name, func
        self.timeout, self.retries = timeout, retries
        self.deps, self.result = [], None

    async def run(self, context):
        attempt = 0
        while attempt <= self.retries:
            try:
                with async_timeout.timeout(self.timeout):
                    self.result = await self.func(context)
                    return self.result
            except Exception as e:
                logging.warning(f"{self.name} failed: {e}")
                attempt += 1
        raise RuntimeError(f"{self.name} exceeded retries")

class DAG:
    def __init__(self, nodes):
        self.nodes = {n.name: n for n in nodes}

    async def execute(self, context):
        # gather nodes with no deps first
        pending = [n for n in self.nodes.values() if not n.deps]
        done = set()
        while pending:
            # run ready nodes concurrently
            results = await asyncio.gather(*(n.run(context) for n in pending))
            done.update(n.name for n in pending)
            # pick next batch whose deps are satisfied
            pending = [n for n in self.nodes.values()
                       if n.name not in done and all(d in done for d in n.deps)]
        return {n.name: n.result for n in self.nodes.values()}
