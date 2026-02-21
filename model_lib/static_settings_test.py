import os

import pytest
from pytest_model_lib.plugin import skip_unless_env

from model_lib import StaticSettings


@pytest.fixture
def external_api_key():
    return skip_unless_env("EXTERNAL_API_KEY")


def test_static_settings_for_testing(tmp_path):
    settings = StaticSettings.for_testing(tmp_path=tmp_path)
    assert settings.STATIC_DIR == tmp_path / "static"
    assert settings.CACHE_DIR == tmp_path / "cache"
    assert settings.STATIC_DIR and settings.STATIC_DIR.exists()
    assert settings.CACHE_DIR and settings.CACHE_DIR.exists()


def test_static_settings_app_name():
    assert StaticSettings.app_name() == "static"


def test_static_settings_roots(tmp_path):
    settings = StaticSettings.for_testing(tmp_path=tmp_path)
    assert settings.STATIC_DIR and settings.static_root == settings.STATIC_DIR / "static"
    assert settings.CACHE_DIR and settings.cache_root == settings.CACHE_DIR / "static"


def test_static_settings_skip_app_name(tmp_path):
    settings = StaticSettings.for_testing(tmp_path=tmp_path, SKIP_APP_NAME=True)
    assert settings.static_root == settings.STATIC_DIR
    assert settings.cache_root == settings.CACHE_DIR


@pytest.mark.manual
def test_with_jira_token_required():
    jira_token = os.environ.get("JIRA_TOKEN")
    assert jira_token
    assert len(jira_token) > 0


@pytest.mark.manual
def test_with_external_api_fixture(external_api_key):
    assert external_api_key
    assert len(external_api_key) > 0
