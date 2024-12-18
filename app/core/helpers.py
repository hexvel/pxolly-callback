from app.http import VKAPIClient


async def search_peer(
    api: VKAPIClient, text: str, from_id: int, date: int, conversation_message_id: int
):
    code = """
        var e = 2000000000;
        var h = API.messages.search({
        q: Args.text,
        count: 5,
        }).items;

        var i = 0;
        while (i < h.length) {
        if (
            h[i].peer_id > e &&
            Args.text == h[i].text &&
            Args.from_id == h[i].from_id &&
            Args.date == h[i].date &&
            Args.conversation_message_id == h[i].conversation_message_id
        ) {
            return h[i].peer_id - e;
        }
        i = i + 1;
        }
        return false;
    """

    peer = await api.execute(
        method="execute",
        params={
            "code": code,
            "text": text,
            "from_id": from_id,
            "date": date,
            "conversation_message_id": conversation_message_id,
        },
    )

    return peer
