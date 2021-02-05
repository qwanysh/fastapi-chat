from secrets import token_hex


def generate_chat_id() -> str:
    return token_hex(8)
