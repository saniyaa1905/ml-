# Job Sequencing using Greedy Method

n = int(input("Enter number of jobs: "))
jobs = []

# Step 1: Accept job details
for i in range(n):
    job = input("Enter job ID: ")
    deadline = int(input("Enter deadline: "))
    profit = int(input("Enter profit: "))
    jobs.append((job, deadline, profit))

# Step 2: Sort jobs by profit
jobs.sort(key=lambda x: x[2], reverse=True)

# Step 3: Create time slots
slots = [None] * max(j[1] for j in jobs)
total_profit = 0

# Step 4: Schedule jobs
for job, deadline, profit in jobs:
    for i in range(min(deadline, len(slots)) - 1, -1, -1):
        if slots[i] is None:
            slots[i] = job
            total_profit += profit
            break

# Step 5: Display result
print("Scheduled Jobs:", [j for j in slots if j])
print("Maximum Profit:", total_profit)