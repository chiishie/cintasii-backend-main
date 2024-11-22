from fastapi import APIRouter

import src.accounts.routes as accounts
import src.roles.routes as roles

router = APIRouter()

router.include_router(accounts.router)

router.include_router(roles.router, prefix="/roles", tags=["roles"])