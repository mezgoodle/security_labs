from django.contrib.sessions.backends.db import SessionStore
from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings

from .utils import refreshToken


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_token, "interval", seconds=30)
    scheduler.start()


def update_token():
    session = SessionStore(session_key=settings.SESSION_KEY)
    try:
        refresh_token = session["refresh_token"]
        _, data = refreshToken(refresh_token)
        session["access_token"] = data["access_token"]
        session.save()
    except KeyError:
        pass
