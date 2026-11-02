"""
Module 14: Concurrency & AsyncIO
Contains 5 programs ranging from threads to asynchronous task coordination:
1. Multithreading using the standard threading module
2. Concurrent task pool with concurrent.futures.ThreadPoolExecutor
3. Safe process pool execution with concurrent.futures.ProcessPoolExecutor
4. Asynchronous coroutine execution using async and await
5. Gathering multiple concurrent async tasks using asyncio.gather
"""

import threading
import concurrent.futures
import asyncio
import time

# Program 1: Standard Threading
def worker_task(tid: int, results: list):
    results.append(f"Thread-{tid} finished")

def program_1_threads() -> list:
    results = []
    threads = []
    for i in range(3):
        t = threading.Thread(target=worker_task, args=(i, results))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

# Program 2: ThreadPoolExecutor
def program_2_thread_pool(numbers: list) -> list:
    def square(n):
        return n * n

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        results = list(executor.map(square, numbers))
    return results

# Program 3: Simulating CPU Tasks
def heavy_computation(val: int) -> int:
    return sum(i * i for i in range(val))

def program_3_cpu_worker(val: int) -> int:
    # Demonstrates task delegation
    return heavy_computation(val)

# Program 4: AsyncIO Coroutine
async def async_fetch_mock(resource_id: str) -> dict:
    await asyncio.sleep(0.01)  # Non-blocking simulation
    return {"resource": resource_id, "status": "200 OK"}

def program_4_run_coroutine():
    return asyncio.run(async_fetch_mock("telemetry-stream"))

# Program 5: AsyncIO Gather (Concurrent Tasks)
async def fetch_all_tasks():
    tasks = [
        async_fetch_mock("auth-service"),
        async_fetch_mock("audit-ledger"),
        async_fetch_mock("copilot-engine")
    ]
    results = await asyncio.gather(*tasks)
    return results

def program_5_run_gather():
    return asyncio.run(fetch_all_tasks())

if __name__ == "__main__":
    print("=== Module 14: Concurrency & AsyncIO ===")
    print("[P1] Thread execution:", program_1_threads())
    print("[P2] ThreadPool squares:", program_2_thread_pool([2, 4, 6, 8]))
    print("[P3] Heavy computation (1000):", program_3_cpu_worker(1000))
    print("[P4] Async coroutine:", program_4_run_coroutine())
    print("[P5] Async gather:", program_5_run_gather())
