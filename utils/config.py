from pydantic_settings import BaseSettings


class Config(BaseSettings):
    jina_api_key: str

    qdrant_url: str = ":memory:"
    qdrant_api_key: str | None = None
    qdrant_collection_name: str = "papers"
    proxy_base_url: str = "https://http-proxy.up.railway.app"
    pdf2md_base_url: str = "https://pdf2md.up.railway.app"

    model_config = {"env_file": ".env"}


env = Config()  # type: ignore
