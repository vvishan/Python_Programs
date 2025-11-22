def queue_length(arrival_times, s):
    end_time = 0
    queue = 0
    max_queue = 0

    for t in arrival_times:
        # Process completed requests before new arrival
        if t >= end_time:
            queue = 0
            end_time = t + s
        else:
            queue += 1
            end_time += s
        max_queue = max(max_queue, queue)

    return max_queue