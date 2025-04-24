import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI

sys.path.append(str(Path(__file__).parent.parent))

from src.api.auth import router as router_auth




app = FastAPI(title='BELS-SHOP Docs')

app.include_router(router_auth)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)