import sys
from pathlib import Path

import uvicorn
from fastapi import FastAPI


sys.path.append(str(Path(__file__).parent.parent))


app = FastAPI(title='BELS-SHOP Docs')


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)