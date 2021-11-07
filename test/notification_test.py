from . import context
import sqlite3
import pytest
from .utils import *
from typing import Optional

SAMPLE_SELF_USERNAME: str = "self username"
SAMPLE_SELF_FIRSTNAME: str = "self firstname"
SAMPLE_SELF_LASTNAME: str = "self lastname"
SAMPLE_FRIEND_USERNAME: str = "friend username"
SAMPLE_FRIEND_FIRSTNAME: str = "friend firstname"
SAMPLE_FRIEND_LASTNAME: str = "friend lastname"
SAMPLE_PASSWORD: str = "P@ssword12"
mock_db: Optional[sqlite3.Connection] = None
cursor: Optional[sqlite3.Cursor] = None


@pytest.fixture(autouse=True)
def run_around_tests(monkeypatch) -> None:
    global mock_db, cursor
    mock_db = get_mock_db()
    cursor = mock_db.cursor()
    add_user(mock_db, SAMPLE_SELF_USERNAME, SAMPLE_PASSWORD,
             SAMPLE_SELF_FIRSTNAME, SAMPLE_SELF_LASTNAME)
    add_user(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_PASSWORD,
             SAMPLE_FRIEND_FIRSTNAME, SAMPLE_FRIEND_LASTNAME)
    monkeypatch.setattr('src.friends.c', mock_db.cursor())

    yield

    mock_db.close()


def application_drought_test(capsys):
    login_user(mock_db, SAMPLE_SELF_USERNAME)
    output = capsys.readouterr()
    assert output.out == "Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!"



def new_messages_notif_test(capsys):
    add_new_message(mock_db, SAMPLE_FRIEND_USERNAME, SAMPLE_SELF_USERNAME, "Hello World!")
    login_user(mock_db, SAMPLE_SELF_USERNAME)
    output = capsys.readouterr()
    unread_message_count = 1
    assert output.out == f"You have {unread_message_count} unread messages\n"

