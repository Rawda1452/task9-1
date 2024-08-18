def min_removals_to_equal_frequency(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    freq_count = {}
    for freq in char_count.values():
        if freq in freq_count:
            freq_count[freq] += 1
        else:
            freq_count[freq] = 1
    
    if len(freq_count) == 1:
        return 0
    
    min_removals = float('inf')

    for freq in freq_count:
        current_removals = 0
        for char_freq, count in freq_count.items():
            if char_freq != freq:
                if char_freq > freq:
                    current_removals += (char_freq - freq) * count
                else:
                    current_removals += char_freq * count
        
        min_removals = min(min_removals, current_removals)
    
    return min_removals

input_string = input("Enter the string: ")
print(f"Minimum removals to make frequencies equal: {min_removals_to_equal_frequency(input_string)}")
