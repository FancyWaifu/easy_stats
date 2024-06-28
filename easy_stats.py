import statistics
import numpy as np
import pandas as pd

print(" ___                       _           _       ")
print("| __> ___  ___ _ _   ___ _| |_  ___  _| |_  ___")
print("| _> <_> |<_-<| | | <_-<  | |  <_> |  | |  <_-<")
print("|___><___|/__/`_. | /__/  |_|  <___|  |_|  /__/")
print("              <___'                             ")

def calc_stats(num_arry):
    mean_value = statistics.mean(numbers)
    median_value = statistics.median(numbers)
    try:
        mode_value = statistics.mode(numbers)
    except:
        mode_value = "No unique mode found"
    range_value = max(numbers) - min(numbers)  
    return mean_value, median_value, mode_value, range_value

def calc_std_dev(num_arry):
    return statistics.stdev(num_arry), statistics.variance(num_arry)

def z_score_calc(num_arry, mean, stddev):
    numbers = []
    for x in num_arry:
        value = (x - mean) / stddev
        numbers.append(value)  
    return numbers

def calculate_quartiles(num_arry):
    q1 = statistics.quantiles(num_arry, n=4)[0]  
    q2 = statistics.median(num_arry)             
    q3 = statistics.quantiles(num_arry, n=4)[2]  
    q4 = max(num_arry)                           
    return q1, q2, q3, q4

def calc_freq(num_arry):
    data = np.array(num_arry)

    frequency = np.bincount(data)

    unique_numbers = np.nonzero(frequency)[0]

    total_count = len(data)

    relative_frequency = frequency[unique_numbers] / total_count

    cumulative_frequency = np.cumsum(frequency[unique_numbers])

    cumulative_relative_frequency = np.cumsum(relative_frequency)

    df = pd.DataFrame({
    'Number': unique_numbers,
    'Frequency': frequency[unique_numbers],
    'Relative Frequency': relative_frequency,
    'Cumulative Frequency': cumulative_frequency,
    'Cumulative Relative Frequency': cumulative_relative_frequency
    })

    print(df)


numbers = [84, 88, 69, 73, 49, 75, 74, 65, 77, 73, 82, 67, 72, 70, 64, 76, 91, 95, 75, 83, 79, 77, 91, 75, 94, 55, 93, 68, 86, 82, 61, 69, 73, 88, 61, 92, 44, 87, 59, 93]

mean_value, median_value, mode_value, range_value = calc_stats(numbers)
std_dev, variance = calc_std_dev(numbers)

z_score = z_score_calc(numbers, mean_value, std_dev)

q1, q2, q3, q4 = calculate_quartiles(numbers)

print("Mean: " + str(mean_value))
print("Median: " + str(median_value))
print("Mode: " + str(mode_value))
print("Range: " + str(range_value))
print("--------------------------")
print("Variance: " + str(variance))
print("Standard deviation: " + str(std_dev))
print("Z scores for all X values: ")
for x in range(len(z_score)):
    print(str(numbers[x]) + " ---> " + str(z_score[x]))
print("--------------------------")
print(f"Q1 (25th percentile): {q1}")
print(f"Q2 (50th percentile, Median): {q2}")
print(f"Q3 (75th percentile): {q3}")
print(f"Q4 (Maximum value): {q4}")
print("--------------------------")
calc_freq(numbers)