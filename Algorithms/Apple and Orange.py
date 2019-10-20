pair_input = lambda: map(int, input().split())

def count_in_range(fruit_count, tree_pos):
    ranges = list(map(int, input().split()))
    in_range = 0

    for r in ranges:
        fall_dist = tree_pos + r
        in_range += house_start <= fall_dist <= house_end
    
    return in_range

house_start, house_end = pair_input()
apple_tree, orange_tree = pair_input()
apple_count, orange_count = pair_input()
apples_in_range = count_in_range(apple_count, apple_tree)
orange_in_range = count_in_range(orange_count, orange_tree)

print(apples_in_range)
print(orange_in_range)