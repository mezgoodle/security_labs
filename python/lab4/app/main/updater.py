from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from apscheduler.schedulers.background import BackgroundScheduler

from .utils import refreshToken


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_token, "interval", seconds=30)
    scheduler.start()


def update_token():
    session = SessionStore(session_key="ezfrews0mtg9a9nzjdpg53mpyaryh3a8")
    try:
        refresh_token = session["refresh_token"]
        _, data = refreshToken(refresh_token)
        session["access_token"] = data["access_token"]
        session.save()
    except KeyError:
        pass
