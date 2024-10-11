import os

def check_environment_variables():
    # List of required environment variables
    required_env_vars = [
        'TELEGRAM_TOKEN',
        'CHAT_ID',
        'DISCORD_WEBHOOK_URL',
    ]

    for var in required_env_vars:
        value = os.getenv(var)
        if value:
            print(f"{var}: {value}")
        else:
            print(f"Warning: {var} is not set.")

if __name__ == '__main__':
    check_environment_variables()
