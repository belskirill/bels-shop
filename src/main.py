import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.auth import router as router_auth
from src.api.users import router as router_users




app = FastAPI(title='BELS-SHOP Docs')

app.include_router(router_auth)
app.include_router(router_users)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)