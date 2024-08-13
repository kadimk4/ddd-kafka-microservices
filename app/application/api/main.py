from fastapi import Depends, FastAPI

from application.api.user.user_router import router as user_router


app = FastAPI(title="ddd-kafka-microservices", debug=True)
app.include_router(user_router, prefix="/user")
