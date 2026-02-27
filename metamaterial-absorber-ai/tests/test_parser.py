from app.utils.cst_parser import parse_cst_export


def test_parse_cst_export(tmp_path):
    fixture = tmp_path / "sample.txt"
    fixture.write_text("name: design-1\nfrequency: 10.5 GHz\n")

    parsed = parse_cst_export(fixture)

    assert parsed["name"] == "design-1"
    assert parsed["frequency"] == "10.5 GHz"
