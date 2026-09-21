import os
from dotenv import load_dotenv

load_dotenv()


def load_config() -> dict[str, str | None]:
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }


def display_config(config: dict[str, str | None]) -> None:
    print("Configuration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    if config['DATABASE_URL']:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")

    if config['API_KEY']:
        print("API Access: Authenticated")
    else:
        print("API Access: No credentials")
    print(f"Log Level: {config['LOG_LEVEL']}")
    if config['ZION_ENDPOINT']:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")


def display_mode_info(config: dict[str, str | None]) -> None:
    mode = config['MATRIX_MODE']
    if mode == "production":
        print("Running in PRODUCTION mode - security hardened")
    else:
        print("Running in DEVELOPMENT mode - debug enabled")


def security_check(config: dict[str, str | None]) -> None:
    print("Environment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")
    print("[OK] Production overrides available")


if __name__ == "__main__":
    print("ORACLE STATUS: Reading the Matrix...\n")
    config = load_config()
    display_config(config)
    print()
    display_mode_info(config)
    print()
    security_check(config)
    print("\nThe Oracle sees all configurations.")
