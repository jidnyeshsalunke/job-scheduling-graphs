# job-scheduling-graphs
A Python implementation of job scheduling using Directed Acyclic Graphs (DAGs) and topological sorting. This Data Structures mini project schedules dependent jobs in the correct execution order using graph algorithms.

# Job Scheduling Using Graphs

## Project Information
- Subject: Data Structures
- Course: SPPU SE Computer Engineering
- Programming Language: Python
- Concepts: Graphs, BFS, Topological Sorting

## Abstract
This project implements job scheduling using a directed
graph. Each job is represented as a vertex, and each
dependency is represented as a directed edge.

The program uses topological sorting with a queue to
determine a valid execution order for the jobs. It also
detects circular dependencies, which prevent a valid
schedule from being generated.

## Objectives
- Understand graph representation using adjacency lists.
- Implement topological sorting.
- Schedule dependent jobs in the correct order.
- Detect cycles in job dependencies.

## Data Structures Used
- Dictionary: Stores the adjacency list and indegrees.
- List: Stores jobs and the final schedule.
- Queue: Processes jobs whose dependencies are complete.

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in VS Code.
4. Run:

   python job_scheduling_graphs.py

## Algorithm
Kahn's Algorithm for Topological Sorting.

## Complexity Analysis
Time Complexity: O(V + E)
Space Complexity: O(V + E)

V = Number of jobs (vertices)
E = Number of dependencies (edges)

## Applications
- Project task scheduling.
- Build systems and software compilation.
- Course prerequisite planning.
- Workflow and process management.

## Conclusion
This project demonstrates how graph algorithms can
schedule dependent jobs in a valid order. Topological
sorting ensures that each job is scheduled only after
its prerequisite jobs have been completed.
```

## 5. Sample output

```text
Job Scheduling using Graphs
----------------------------
Total jobs: 6

Valid execution order:
Step 1: A
Step 2: B
Step 3: C
Step 4: D
Step 5: E
Step 6: F
```

A valid execution order can vary depending on the order in which independent jobs enter the queue. The output above is one possible order.

## 6. Graph representation

<box border radius="lg" padding={3} align="center" gap={2}>
  <svg viewBox="0 0 320 205" width="100%" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow" markerWidth="7" markerHeight="7" refX="6" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z" fill="currentColor"/></marker>
    </defs>
    {#each [{x1:50,y1:34,x2:103,y2:81},{x1:50,y1:34,x2:180,y2:81},{x1:153,y1:94,x2:205,y2:130},{x1:230,y1:94,x2:230,y2:130},{x1:220,y1:143,x2:150,y2:176}] as a}
      <line x1={a.x1} y1={a.y1} x2={a.x2} y2={a.y2} stroke="currentColor" strokeWidth="1.5" markerEnd="url(#arrow)"/>
    {/each}
    <g fill="#DCEAFE" stroke="#3974C6" strokeWidth="1.5">
      <circle cx="38" cy="25" r="17"/><circle cx="118" cy="92" r="17"/><circle cx="220" cy="92" r="17"/><circle cx="220" cy="143" r="17"/><circle cx="137" cy="180" r="17"/>
    </g>
    <g fill="#15365D" fontSize="13" textAnchor="middle" dominantBaseline="middle" fontWeight="600">
      <text x="38" y="25">A</text><text x="118" y="92">C</text><text x="220" y="92">D</text><text x="220" y="143">E</text><text x="137" y="180">F</text>
    </g>
    <g fill="currentColor" fontSize="12">
      <text x="4" y="57">B → D</text>
    </g>
  </svg>
  <text color="secondary" size="sm">Illustration of job dependencies. An arrow A → C means job A must finish before job C.</text>
</box>

## 7. GitHub topics

`python` · `data-structures` · `graphs` · `job-scheduling` · `topological-sort` · `dag` · `sppu`

## 8. Upload to GitHub

1. Open <Link url="https://github.com/new" title="GitHub — Create a new repository"/>.
2. Enter `job-scheduling-graphs` as the repository name.
3. Add the repository description from Section 1.
4. Choose **Public** if you want to showcase the project.
5. Create the repository and add `job_scheduling_graphs.py` and `README.md`.
6. Click **Commit changes**.

**Important:** This project schedules jobs based on dependencies, not based on execution time or profit. It uses Kahn's topological sorting algorithm and detects cycles in the dependency graph.