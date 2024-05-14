import sys

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file]
    return requests

def fcfs(requests, initial_position):
    head_movement = 0
    current_position = initial_position
    for request in requests:
        head_movement += abs(request - current_position)
        current_position = request
    return head_movement

def scan(requests, initial_position, total_cylinders=5000):
    requests.sort()
    head_movement = 0
    current_position = initial_position
    index = 0
    
    # Find the first request greater than or equal to the initial position
    while index < len(requests) and requests[index] < initial_position:
        index += 1
    
    # Move to the right towards the outermost cylinder
    for i in range(index, len(requests)):
        head_movement += abs(requests[i] - current_position)
        current_position = requests[i]
    
    # Move to the left towards the innermost cylinder
    if index > 0:
        head_movement += abs(current_position - requests[index - 1])
        current_position = requests[index - 1]
        for i in range(index - 2, -1, -1):
            head_movement += abs(requests[i] - current_position)
            current_position = requests[i]

    return head_movement

def c_scan(requests, initial_position, total_cylinders=5000):
    requests.append(total_cylinders - 1)
    requests.append(0)
    requests.sort()
    head_movement = 0
    current_position = initial_position
    index = 0

    # Find the first request greater than or equal to the initial position
    while index < len(requests) and requests[index] < initial_position:
        index += 1
    
    # Move to the right till the end
    for i in range(index, len(requests)):
        head_movement += abs(requests[i] - current_position)
        current_position = requests[i]

    # Start from the beginning to the initial right request
    if index > 0:
        head_movement += abs(current_position - requests[0])
        current_position = requests[0]
        for i in range(1, index):
            head_movement += abs(requests[i] - current_position)
            current_position = requests[i]

    return head_movement

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python disk_scheduling.py <initial_head_position>")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    requests_file = "C:\\CODES\\OS\\requests.txt"  # Hardcoded path to the file
    requests = read_requests(requests_file)

    print("FCFS Head Movements:", fcfs(requests, initial_head_position))
    print("SCAN Head Movements:", scan(requests, initial_head_position))
    print("C-SCAN Head Movements:", c_scan(requests, initial_head_position))
