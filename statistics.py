
def calculateStats(numbers):
    if len(numbers) == 0:
        stat_dict = {"avg": "nan", "max": "nan", "min": "nan"}
    else:
        max_value = max(numbers)
        min_value = min(numbers)
        avg_value = round(sum(numbers) / len(numbers), 3)
        stat_dict = {"avg": avg_value, "max": max_value, "min": min_value}
    return stat_dict
