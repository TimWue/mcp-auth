from mcp.server.fastmcp import FastMCP
from mcp.server.auth.provider import AccessToken, TokenVerifier
from mcp.server.auth.settings import AuthSettings
from pydantic import AnyHttpUrl


class SimpleTokenVerifier(TokenVerifier):
    async def verify_token(self, token: str) -> AccessToken | None:
        pass


mcp = FastMCP(
    "Hello World",
    token_verifier=SimpleTokenVerifier(),
    auth=AuthSettings(
        issuer_url=AnyHttpUrl("auth-server-url"),
        resource_server_url=AnyHttpUrl("http://localhost:8000"),
        required_scopes=["user"],
    ),
)


@mcp.tool()
def add(x: int, y: int):
    """Add two numbers"""
    return int(x + y)
