from flask import Flask
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# KeyVault bağlantısı
keyvault_url = "https://your-keyvault-name.vault.azure.net/"

credential = DefaultAzureCredential()

client = SecretClient(
    vault_url=keyvault_url,
    credential=credential
)

db_password = client.get_secret("db-password").value


@app.route("/hello")
def hello():
    return "Hello! Favorite City Counter API"


@app.route("/cities")
def cities():
    return "Cities endpoint"


if __name__ == "__main__":
    app.run(port=5000)
