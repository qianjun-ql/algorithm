def compute_makespan(times, m, assign):
    # times is an array of job times of size n
    # m is the number of processors
    # assign is an array of size n whose entries are between 0 to m-1 
    # indicating the processor number for
    # the corresponding job.
    # Return: makespan of the assignment
    # your code here
    processor_times = [0] * m
    for job, processor in enumerate(assign):
        processor_times[processor] += times[job]
    return max(processor_times)


    print('Test 1 ... ', end = '')
    times = [2, 2, 2, 2, 3, 3, 2]
    assigns = [0, 0, 0, 0, 1, 1, 2]
    m = 3
    s = compute_makespan(times, m, assigns)
    assert s == 8, f'Expected makespan is 8, your code returned: {s}'
    print(' passed!')

    print('Test 2 ...', end='')
    times = [2, 1, 2, 2, 1, 3, 2, 1, 1, 3]
    assigns = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    m = 3
    s = compute_makespan(times, m, assigns)
    assert s == 10, f' Expected makespan is 10, your code returned {s}'
    print('  passed!')
    print('Tests passed: 10 points!')

## BEGIN TESTS
print('Test 1 ... ', end = '')
times = [2, 2, 2, 2, 3, 3, 2]
assigns = [0, 0, 0, 0, 1, 1, 2]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 8, f'Expected makespan is 8, your code returned: {s}'
print(' passed!')

print('Test 2 ...', end='')
times = [2, 1, 2, 2, 1, 3, 2, 1, 1, 3]
assigns = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
m = 3
s = compute_makespan(times, m, assigns)
assert s == 10, f' Expected makespan is 10, your code returned {s}'
print('  passed!')
print('Tests passed: 10 points!')

## END TESTS