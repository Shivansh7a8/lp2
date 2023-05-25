def job_scheduling(jobs):
    # Sort the jobs based on their finish times
    sorted_jobs = sorted(jobs, key=lambda x: x[1])
    
    # Initialize variables
    selected_jobs = []
    previous_finish_time = 0
    
    # Iterate over the sorted jobs and select non-overlapping jobs
    for job in sorted_jobs:
        start_time, finish_time, value = job
        if start_time >= previous_finish_time:
            selected_jobs.append(job)
            previous_finish_time = finish_time
    
    return selected_jobs

# Example usage
jobs = [(1, 4, 20), (3, 7, 25), (5, 9, 15), (6, 10, 30), (8, 11, 18), (2, 6, 12)]
selected_jobs = job_scheduling(jobs)

# Print the selected jobs
for job in selected_jobs:
    print(f"Start Time: {job[0]}, Finish Time: {job[1]}, Value: {job[2]}")
