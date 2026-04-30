N, M = map(int, input().split())
red_pts = list(map(int, input().split()))
blue_pts = list(map(int, input().split()))

# Create a sorted list of all unique reflection points
all_points = sorted(list(set([0] + red_pts + blue_pts)))

ans = 1 # Start with 1 for the intersection at x = 0
last_diff = 0 # 1 if Red is higher, -1 if Blue is higher, 0 if they are on the same side

for i in range(len(all_points) - 1):
    # Check the state in the middle of this interval
    mid_x = (all_points[i] + all_points[i+1]) / 2
    
    # Calculate which side (0 or 1) each beam is on
    # If it has passed an odd number of reflection points, it's on side 1
    side_r = sum(1 for p in red_pts if p < mid_x) % 2
    side_b = sum(1 for p in blue_pts if p < mid_x) % 2
    
    current_diff = side_r - side_b # Will be 1, -1, or 0
    
    if current_diff != 0:
        if last_diff != 0 and current_diff != last_diff:
            # They swapped sides (one jumped over the other)
            ans += 1
        elif last_diff == 0 and i > 0:
            # They were on the same side and now one moved away
            # In the context of this problem, this follows a "meeting" at the edge
            ans += 1
        last_diff = current_diff
    else:
        # They are now on the same side (0 or 1)
        # This means they met at the edge
        ans += 1
        last_diff = 0

print(ans)