def can_place_cows(stalls, cows, dist):
    # Place the first cow in the first stall
    count = 1
    last_pos = stalls[0]

    # Try placing the remaining cows
    for i in range(1, len(stalls)):
        if stalls[i] - last_pos >= dist:
            count += 1
            last_pos = stalls[i]

            # All cows have been placed
            if count == cows:
                return True

    return False


def aggressive_cows(stalls, cows):
    # Step 1: Sort the stalls
    stalls.sort()

    # Step 2: Define the search space
    low = 1
    high = stalls[-1] - stalls[0]

    # Step 3: Binary Search on answer
    while low <= high:
        mid = low + (high - low) // 2

        if can_place_cows(stalls, cows, mid):
            # Distance is possible, try for a larger one
            low = mid + 1
        else:
            # Distance is not possible, reduce it
            high = mid - 1

    # 'high' stores the largest valid distance
    return high


# Example usage
stalls = [1, 2, 4, 8, 9]
cows = 3

print(aggressive_cows(stalls, cows))  # Output: 3