from database.connection import fetch, execute


async def getEmails():
    query = "SELECT email from users"
    return [dict(x) for x in await fetch(query=query, isOne=False)]