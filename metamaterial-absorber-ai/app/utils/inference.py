def infer_geometry_from_target(target: dict) -> dict:
    """Simple deterministic baseline for inverse-design demo."""
    absorption = float(target.get("absorption", 0.9))
    frequency = float(target.get("frequency", 10.0))
    return {
        "shape": "square_ring",
        "outer_size_mm": round(8 + (1 - absorption) * 10, 3),
        "inner_size_mm": round(3 + (frequency / 20), 3),
        "substrate_thickness_mm": 1.6,
    }
