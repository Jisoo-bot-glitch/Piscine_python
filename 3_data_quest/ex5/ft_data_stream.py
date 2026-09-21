import typing
import random

player_name: list[str] = [
    "bob",
    "alice",
    "dylan",
    "charlie"
]

player_action: list[str] = [
    "run",
    "sleep",
    "grab",
    "eat",
    "move",
    "swim",
    "climb",
    "release"
]


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        name = random.choice(player_name)
        action = random.choice(player_action)
        yield name, action


def consume_event(
    events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while events:
        idx = random.randrange(len(events))
        event = events[idx]
        del events[idx]
        yield event[0], event[1]


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    g = gen_event()
    for i in range(1000):
        event = next((g))
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    event_list = []
    for i in range(10):
        event = next((g))
        event_list.append(event)
    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
