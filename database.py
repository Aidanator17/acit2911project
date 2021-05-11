#DO NOT RUN

from sqlalchemy import Table, Column, String, MetaData, create_engine, ARRAY
import uuid
import os
import re

def dbpush(pn,pc,aic,mov,win,plyd):

    uri = os.getenv("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)

    engine = create_engine(uri, echo=True, future=True)
    metadata = MetaData(engine)

    matches = Table('matches', metadata,
        Column('match_id', String(500), primary_key=True),
        Column('playername', String(500)),
        Column('playercolor', String(5)),
        Column('AIcolor', String(5)),
        Column('moves', ARRAY(String)),
        Column('winner', String(500)),
        Column('played', String(500))
    )

    ins = matches.insert().values(match_id=str(uuid.uuid4()),playername=pn, playercolor=pc, AIcolor=aic, moves=mov, winner=win, played=plyd)

    conn = engine.connect()
    conn.execute(ins)

dbpush('Aidan','White','Black',['white pawn from a2 to a4','black knight from b7 to d6'],'Aidan','2021-05-10 5:31PM')