from app.utils.inference import infer_geometry_from_target
from app.utils.sensing import extract_basic_features


def test_infer_geometry_from_target_returns_expected_keys():
    output = infer_geometry_from_target({"absorption": 0.9, "frequency": 10})
    assert {"shape", "outer_size_mm", "inner_size_mm", "substrate_thickness_mm"}.issubset(output.keys())


def test_extract_basic_features():
    data = [1.0, 2.0, 3.0]
    features = extract_basic_features(data)
    assert features["mean"] == 2.0
    assert features["max"] == 3.0
