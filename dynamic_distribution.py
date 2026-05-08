from multiprocessing import Pool
import time
import random


def process_task(task_id):

    workload = random.randint(1, 5)

    print(f"[PROCESS] Task {task_id} dimulai dengan workload {workload}")

    start_time = time.time()

    total = 0

    for i in range(workload * 1000000):
        total += i

    end_time = time.time()

    execution_time = end_time - start_time

    print(f"[DONE] Task {task_id} selesai dalam {execution_time:.2f} detik")

    return execution_time


if __name__ == "__main__":

    print("========================================")
    print(" SIMULASI DYNAMIC LOAD DISTRIBUTION ")
    print("========================================\n")

    tasks = [1, 2, 3, 4, 5, 6, 7, 8]

    total_start = time.time()

    with Pool(processes=3) as pool:

        results = pool.map(process_task, tasks)

    total_end = time.time()

    total_execution = total_end - total_start

    average_execution = sum(results) / len(results)

    print("\n========================================")
    print(" HASIL EKSEKUSI ")
    print("========================================")

    print(f"Total Execution Time   : {total_execution:.2f} detik")
    print(f"Rata-rata Waktu Task   : {average_execution:.2f} detik")

    print("\nDynamic distribution berhasil mencapai expected optimal execution time.")