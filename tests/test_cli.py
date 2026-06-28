from amazfit2garmin import cli


def test_cli_generates_tcx_files(
    monkeypatch,
    tmp_path,
    running_activity,
    capsys,
):

    input_file = tmp_path / "SPORT.csv"
    input_file.write_text("dummy")

    output_dir = tmp_path / "output"

    written = []

    monkeypatch.setattr(
        "amazfit2garmin.cli.parse_csv",
        lambda _: [running_activity],
    )

    class DummyWriter:

        def write(
            self,
            activity,
            output_path,
        ):
            written.append(output_path)

    monkeypatch.setattr(
        "amazfit2garmin.cli.TcxWriter",
        DummyWriter,
    )

    monkeypatch.setattr(
        "sys.argv",
        [
            "amazfit2garmin",
            str(input_file),
            str(output_dir),
        ],
    )

    result = cli.main()

    captured = capsys.readouterr()

    assert result == 0

    assert len(written) == 1

    assert written[0].name.endswith(".tcx")

    assert "Loaded activities : 1" in captured.out

    assert "Generated files   : 1" in captured.out


def test_cli_missing_input_file(
    monkeypatch,
    tmp_path,
    capsys,
):

    missing = tmp_path / "missing.csv"

    monkeypatch.setattr(
        "sys.argv",
        [
            "amazfit2garmin",
            str(missing),
            str(tmp_path),
        ],
    )

    result = cli.main()

    captured = capsys.readouterr()

    assert result == 1

    assert "Input file not found" in captured.out