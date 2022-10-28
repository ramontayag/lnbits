import asyncio

from fastapi import APIRouter

from lnbits.db import Database
from lnbits.helpers import template_renderer

db = Database("ext_electrosats")

electrosats_ext: APIRouter = APIRouter(prefix="/electrosats", tags=["electrosats"])


def electrosats_renderer():
    return template_renderer(["lnbits/extensions/electrosats/templates"])


from .views import *  # noqa
from .views_api import *  # noqa
