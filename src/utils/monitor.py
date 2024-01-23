import time
import psutil
import os
from prettytable import PrettyTable

def monitor(func):
    def wrapper(*args, **kwargs):
        # Memory usage before function execution
        mem_before = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

        # CPU usage before function execution
        cpu_before = psutil.cpu_percent(interval=None)

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        # Memory usage after function execution
        mem_after = psutil.Process(os.getpid()).memory_info().rss / 1024 / 1024

        # CPU usage after function execution
        cpu_after = psutil.cpu_percent(interval=None)

        execution_time = (end_time - start_time) * 1000  # convert to milliseconds

        # Create a table
        table = PrettyTable()

        # Add columns
        table.field_names = ["Metric", "Value"]
        table.add_row(["Execution time (ms)", f"{execution_time:.2f}"])
        table.add_row(["Memory used (MB)", f"{mem_after - mem_before:.2f}"])
        table.add_row(["CPU used (%)", f"{cpu_after - cpu_before:.2f}"])

        print(table)

        return result
    return wrapper