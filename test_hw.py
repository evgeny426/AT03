import pytest
from main_hw import get_cat


def test_get_cat_success(mocker):
    mock_get = mocker.patch('main_hw.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "id":"MTcwMTAxNg",
        "url":"https://cdn2.thecatapi.com/images/MTcwMTAxNg.png",
        "width":500,
        "height":318
    }

    cat_data = get_cat()

    assert cat_data == {
        "id":"MTcwMTAxNg",
        "url":"https://cdn2.thecatapi.com/images/MTcwMTAxNg.png",
        "width":500,
        "height":318
    }


def test_get_github_user_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404


    cat_data = get_cat()

    assert cat_data == None