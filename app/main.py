import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import donations, distributions, report, database


app = FastAPI(
    title="Shelter",
    summary="This project is a basic donation inventory management application.",
    version="0.0.1",
    contact={
        "name": "Dillon",
        "email": "dillon.oleary@icloud.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/license/mit/",
    },
)

app.include_router(donations.router)
app.include_router(distributions.router)
app.include_router(report.router)
app.include_router(database.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# for debugging purposes
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
