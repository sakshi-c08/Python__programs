#WAP to find the majority element in an array(usng Moore's voting algorithm)

def majority_element(arr):
    count = 0
    candidate = None

    # Step 1: Find candidate
    for num in arr:
        if count == 0:
            candidate = num
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Step 2: Verify candidate
    if arr.count(candidate) > len(arr) // 2:
        return candidate
    else:
        return "No Majority Element"
arr = [3,3,4,2,4,4,2,4,4]
print("Majority Element : ",majority_element(arr))
