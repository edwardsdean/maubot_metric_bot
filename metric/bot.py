from .unitconversion import *
from mautrix.types import RoomID, ImageInfo, EventType, StateEvent, TextMessageEventContent, Event, ReactionEvent, RelationType, MessageType
from maubot import Plugin, MessageEvent
from maubot.handlers import command, event


class MetricPlugin(Plugin):
    @classmethod
    @event.on(EventType.ROOM_MESSAGE)
    async def on_imperial_message(self, evt: MessageEvent) -> None:
        if evt.content.msgtype != MessageType.TEXT or evt.content.body.startswith("!") or evt.content.body.startswith("."):
            return

        message = evt.content.body
        converted_message = process(message)

        if type(converted_message) is str: ## if message doesnt get converter it is None Type object
            await evt.reply(content=TextMessageEventContent(msgtype=MessageType.TEXT, body=converted_message))
