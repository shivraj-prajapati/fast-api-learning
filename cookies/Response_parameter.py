from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/set-cookie")
def set_secure_cookie(response: Response):
    # Set a secure cookie with all important attributes
    response.set_cookie(
        key="key_1",         # Cookie ka naam
        value="mai Hu Cookie NUmber 1",           # Cookie ka value
        max_age=3600,                   # Cookie 1 ghante ke liye valid rahegi (3600 seconds)
        expires=3600,                   # Cookie 1 ghante me expire ho jayegi
        httponly=True,                  # JavaScript ke through access nahi hogi (XSS se protection)
        secure=False,                    # Sirf HTTPS ke through send hogi
        samesite="Lax"                  # CSRF se protection ke liye, "Strict", "Lax", ya "None" use kar sakte hain
    )
    return {"message": "Secure cookie set successfully"}

@app.get("/get-cookie")
def get_cookie():
    return {"message": "Check your cookies!"}

if __name__ == "__main__":
    import uvicorn 
    uvicorn.run(app, host="127.0.0.1", port=8080)