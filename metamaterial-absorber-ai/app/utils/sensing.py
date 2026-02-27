from math import sqrt


def extract_basic_features(signal) -> dict:
    values = [float(x) for x in signal]
    n = len(values)
    mean = sum(values) / n if n else 0.0
    variance = sum((x - mean) ** 2 for x in values) / n if n else 0.0
    return {
        "mean": mean,
        "std": sqrt(variance),
        "max": max(values) if values else 0.0,
        "min": min(values) if values else 0.0,
    }
