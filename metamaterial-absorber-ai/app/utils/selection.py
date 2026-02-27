def top_n_designs(rows, target_col: str, n: int = 5):
    """Return top-N rows by target_col from a DataFrame-like object."""
    if hasattr(rows, "sort_values"):
        return rows.sort_values(target_col, ascending=False).head(n).reset_index(drop=True)
    sorted_rows = sorted(rows, key=lambda r: r[target_col], reverse=True)
    return sorted_rows[:n]
