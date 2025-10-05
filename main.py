from fastmcp import FastMCP
from fastmcp.server.auth.oidc_proxy import OIDCProxy
from dotenv import load_dotenv
import os


# Load client secret from .env
load_dotenv()
if not os.getenv("CLIENT_SECRET"):
    raise Exception("Client secret not defined!")

# Create the OIDC proxy
auth = OIDCProxy(
    # Provider's configuration URL
    config_url="http://localhost:8080/realms/mcp-realm/.well-known/openid-configuration",
    # Your registered app credentials
    client_id="mcp-client",
    client_secret=os.getenv("CLIENT_SECRET"),
    # Your FastMCP server's public URL
    base_url="http://localhost:8000",
    # Optional: customize the callback path (default is "/auth/callback")
    # redirect_path="/custom/callback",
)

mcp = FastMCP(name="My Server", auth=auth)

if __name__ == "__main__":
    mcp.run(transport="http")
