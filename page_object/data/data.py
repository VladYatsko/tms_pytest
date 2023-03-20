from dataclasses import dataclass


@dataclass
class Email:
    email: str = None
    password: str = None
    