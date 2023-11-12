from collections import defaultdict

def get_statistics(input_list):
    # Write your code here.
    sorted_input = sorted(input_list)
    input_len = len(sorted_input)

    # 1. mean
    mean = sum(sorted_input) / input_len

    # 2. median
    left = 0
    right = input_len - 1
    middle_idx = left + (right - left) // 2

    # Odd len
    median = sorted_input[middle_idx]

    # Even len
    if input_len % 2 == 0:
        middle_number_1 = sorted_input[middle_idx]
        middle_number_2 = sorted_input[middle_idx + 1]

        median = (middle_number_1 + middle_number_2) / 2

    # 3. mode
    number_count = defaultdict(int)
    for number in set(sorted_input):
        count = sorted_input.count(number)
        number_count[number] = count

    print(number_count)
    
    mode = sorted_input[0]
    max_count = 0
    for number, count in number_count.items():
        if count > max_count:
            max_count = count
            mode = number

    print(mode)

    # 4. sample_variance or Standard distribution
    sample_variance = 0
    for number in sorted_input:
        sd = ((number - mean) ** 2) /  (input_len - 1)
        sample_variance += sd

    print(sample_variance)

    # 5. Sample standard Deviation
    '''Square root of sample_variance'''
    sample_standard_deviation = (sample_variance) ** 0.5

    # 6. mean_confidence_interval
    
    # a. Sample Standard error
    standar_error = sample_standard_deviation / (input_len ** 0.5)

    # b. Z-score
    z_score = 1.96

    # c. mean_confidence_interval
    mean_confidence_interval = [
        mean - (z_score * standar_error),
        mean + (z_score * standar_error)
    ]



    
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval,
    }
