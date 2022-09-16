from aiogram.dispatcher.router import Router
from bot.filters.chat_type import ChatType

from .create_script import create_script_router
from .control_script_panel import control_script_panel_router
from .control_point import control_point_router
from .edit_script import edit_script_router
from .delete_script import delete_script_router

control_script_router = Router()
control_script_router.message.bind_filter(ChatType)

control_script_router.include_router(create_script_router)
control_script_router.include_router(control_script_panel_router)
control_script_router.include_router(control_point_router)
control_script_router.include_router(edit_script_router)
control_script_router.include_router(delete_script_router)
