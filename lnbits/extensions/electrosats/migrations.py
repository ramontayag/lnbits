# async def m001_initial(db):
#    await db.execute(
#        f"""
#        CREATE TABLE electrosats.electrosats (
#            id TEXT PRIMARY KEY,
#            wallet TEXT NOT NULL,
#            time TIMESTAMP NOT NULL DEFAULT {db.timestamp_now}
#        );
#    """
#    )
