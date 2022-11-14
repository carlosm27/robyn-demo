from robyn import Robyn
from dotenv import load_dotenv
import os

load_dotenv()

PORT = os.environ.get("PORT")

app = Robyn(__file__)

@app.get("/")
async def h(request):
    return "Hello, world!"

app.start("0.0.0.0":PORT)