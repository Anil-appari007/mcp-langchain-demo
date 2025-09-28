### Steps to reproduce

`uv venv`<br>
`.venv\Scripts\activate`<br>

`uv add "mcp[cli]"`<br>
`uv add -r requirements.txt`<br>

#### Start Math mcp server
`python math_server.py`<br>

#### Start weather mcp server
`python weather_server.py`<br>

#### Run the client
`python client.py` <br>