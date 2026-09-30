def calculate_mean(data: list[float]) -> float:
    """Calculate the mean of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The mean of the numbers.
    """
    if not data:
        return 0
    return sum(data) / len(data)


def calculate_variance(data: list[float]) -> float:
    """Calculate the variance of a list of numbers.

    Args:
        data (list): A list of numbers.

    Returns:
        float: The variance of the numbers.
    """
    if not data:
        return 0
    mean = calculate_mean(data)
    return sum((x - mean) ** 2 for x in data) / len(data)
