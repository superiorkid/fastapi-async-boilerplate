from fastapi import FastAPI


def create_application():
    application = FastAPI(title="FastAPI boilerplate")

    @application.get("/health-check")
    def health_check():
        return {"status": "ok"}

    return application


app = create_application()
