
from collections import deque


def job_scheduling(jobs, dependencies):
    # Create adjacency list and indegree table
    graph = {job: [] for job in jobs}
    indegree = {job: 0 for job in jobs}

    # Add dependency edges: job A must finish before B
    for before, after in dependencies:
        graph[before].append(after)
        indegree[after] += 1

    # Queue jobs with no dependencies
    queue = deque(
        job for job in jobs if indegree[job] == 0
    )

    schedule = []

    while queue:
        current = queue.popleft()
        schedule.append(current)

        for neighbor in graph[current]:
            indegree[neighbor] -= 1

            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Detect circular dependencies
    if len(schedule) != len(jobs):
        print("Error: Circular dependency detected!")
        print("No valid schedule exists.")
    else:
        print("Job Scheduling using Graphs")
        print("----------------------------")
        print("Total jobs:", len(jobs))
        print("\nValid execution order:")

        for step, job in enumerate(schedule, start=1):
            print(f"Step {step}: {job}")


if __name__ == "__main__":
    jobs = ["A", "B", "C", "D", "E", "F"]

    # Each pair means the first job must finish
    # before the second job can start.
    dependencies = [
        ("A", "C"),
        ("A", "D"),
        ("B", "D"),
        ("C", "E"),
        ("D", "E"),
        ("E", "F")
    ]

    job_scheduling(jobs, dependencies)
