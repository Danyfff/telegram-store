from .start import router as start_router
from .catalog import router as catalog_router
from .admin import router as admin_router
from .order import router as order_router
from .help import router as help_router

def register_all_routers(dp):
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(admin_router)
    dp.include_router(order_router)
    dp.include_router(help_router)