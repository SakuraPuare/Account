# coding=utf-8
from fastapi import APIRouter

from .admin import admin_router
from .root import root_router
from .user import user_router

router = APIRouter()

router.include_router(root_router)
router.include_router(admin_router)
router.include_router(user_router)
