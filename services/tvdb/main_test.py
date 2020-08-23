# doc: https://click.palletsprojects.com/en/7.x/testing/

from click.testing import CliRunner
from main import delete, update


def test_update_all():
    runner = CliRunner()
    result = runner.invoke(update)
    assert result.exit_code == 0
    assert result.output == 'Updating all series...\n'


def test_update_single():
    runner = CliRunner()
    result = runner.invoke(update, ['--id', '1234'])
    assert result.exit_code == 0
    assert result.output == 'Updating series 1234...\n'


def test_delete_id():
    runner = CliRunner()
    result = runner.invoke(delete, ['1234'])
    assert result.exit_code == 0
    assert result.output == 'Deleting series 1234...\n'


if __name__ == "__main__":
    test_update_all()
    test_update_single()
    test_delete_id()
