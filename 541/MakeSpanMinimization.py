def greedy_makespan_min(times, m):
    import heapq

    # Initialize priority queue to keep track of processor loads
    processor_loads = [(0, i) for i in range(m)]  # (current load, processor index)
    heapq.heapify(processor_loads)

    # Initialize assignment list
    assignment = [-1] * len(times)

    # Assign each job to the least loaded processor
    for i, time in enumerate(times):
        load, processor = heapq.heappop(processor_loads)  # Get the least loaded processor
        assignment[i] = processor
        heapq.heappush(processor_loads, (load + time, processor))  # Update load and reinsert

    # The makespan is the maximum load in the priority queue
    makespan = max(load for load, _ in processor_loads)

    return assignment, makespan

## BEGIN TESTS
def do_test(times, m, expected):
    (a, makespan) = greedy_makespan_min(times,m )
    print('\t Assignment returned: ', a)
    print('\t Claimed makespan: ', makespan)
    assert compute_makespan(times, m, a) == makespan, 'Assignment returned is not consistent with the reported makespan'
    assert makespan == expected, f'Expected makespan should be {expected}, your core returned {makespan}'
    print('Passed')
print('Test 1:')
times = [2, 2, 2, 2, 2, 2, 2, 2, 3] 
m = 3
expected = 7
do_test(times, m, expected)

print('Test 2:')
times = [1]*20 + [5]
m = 5
expected =9
do_test(times, m, expected)

print('Test 3:')
times = [1]*40 + [2]
m = 20
expected = 4
do_test(times, m, expected)
print('All tests passed: 15 points!')
## END TESTS