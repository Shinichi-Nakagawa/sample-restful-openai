from typing import List, Any
import pytest
from ai.interface import RequestForm
from ai.schema import Message

TESTCASE_OK_MESSAGES: List[List[Message]] = [
    [
        Message(index=-33, role="system", content="nandeya"),
        Message(index=-4, role="system", content="hanshin"),
        Message(index=-1, role="system", content="kankeinaiyaro"),
        Message(index=0, role="user", content="hello"),
        Message(index=0, role="assistant", content="world"),
    ]
]

TESTCASE_NG_ROLE_MESSAGES: List[Any] = [
    [
        [
            Message(index=-33, role="ai", content="nandeya"),
            Message(index=-4, role="system", content="hanshin"),
            Message(index=-1, role="system", content="kankeinaiyaro"),
            Message(index=0, role="user", content="hello"),
            Message(index=0, role="assistant", content="world"),
        ],
        "ai",
    ],
    [
        [
            Message(index=-33, role="system", content="nandeya"),
            Message(index=-4, role="chat", content="hanshin"),
            Message(index=-1, role="system", content="kankeinaiyaro"),
            Message(index=0, role="user", content="hello"),
            Message(index=0, role="assistant", content="world"),
        ],
        "chat",
    ],
    [
        [
            Message(index=-33, role="system", content="nandeya"),
            Message(index=-4, role="system", content="hanshin"),
            Message(index=-1, role="system", content="kankeinaiyaro"),
            Message(index=0, role="person", content="hello"),
            Message(index=0, role="assistant", content="world"),
        ],
        "person",
    ],
    [
        [
            Message(index=-33, role="system", content="nandeya"),
            Message(index=-4, role="system", content="hanshin"),
            Message(index=-1, role="system", content="kankeinaiyaro"),
            Message(index=0, role="user", content="hello"),
            Message(index=0, role="bot", content="world"),
        ],
        "bot",
    ],
]

TESTCASE_NG_CONTENT_MESSAGES: List[List[Message]] = [
    [
        Message(index=-33, role="system", content=""),
        Message(index=-4, role="system", content="hanshin"),
        Message(index=-1, role="system", content="kankeinaiyaro"),
        Message(index=0, role="user", content="hello"),
        Message(index=0, role="assistant", content="world"),
    ],
    [
        Message(index=-33, role="system", content="nandeya"),
        Message(index=-4, role="system", content="hanshin"),
        Message(index=-1, role="system", content="kankeinaiyaro"),
        Message(index=0, role="user", content="hello"),
        Message(index=0, role="assistant", content=""),
    ],
    [
        Message(index=-33, role="system", content="nandeya"),
        Message(index=-4, role="system", content="hanshin"),
        Message(index=-1, role="system", content="kankeinaiyaro"),
        Message(index=0, role="user", content=""),
        Message(index=0, role="assistant", content="world"),
    ],
    [
        Message(index=-33, role="system", content="nandeya"),
        Message(index=-4, role="system", content=""),
        Message(index=-1, role="system", content="kankeinaiyaro"),
        Message(index=0, role="user", content="hello"),
        Message(index=0, role="assistant", content="world"),
    ],
]


@pytest.mark.parametrize("messages", TESTCASE_OK_MESSAGES)
def test_ok_validator(messages: List[Message]) -> None:
    assert messages == RequestForm.validate_messages(messages)


@pytest.mark.parametrize("messages, role", TESTCASE_NG_ROLE_MESSAGES)
def test_ng_validator_role(messages: List[Message], role: str) -> None:
    with pytest.raises(TypeError) as e:
        RequestForm.validate_messages(messages)
    print(e)
    assert str(e.value) == f"Invalid Parameter for role: {role}"


@pytest.mark.parametrize("messages", TESTCASE_NG_CONTENT_MESSAGES)
def test_ng_validator_content(messages: List[Message]) -> None:
    with pytest.raises(ValueError) as e:
        RequestForm.validate_messages(messages)
    print(e)
    assert str(e.value) == "Invalid Parameter for content"
