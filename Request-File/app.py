from typing import Annotated
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

# Endpoint to handle file uploads as raw bytes
@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}

# Endpoint to handle file uploads using UploadFile, which provides more metadata
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)