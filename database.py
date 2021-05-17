#DO NOT RUN

from sqlalchemy import Table, Column, String, MetaData, create_engine, ARRAY
import uuid
from env import uri

def dbpush(pn,pc,aic,mov,win,plyd,tim):

    engine = create_engine(uri(), echo=True)
    metadata = MetaData(engine)

    matches = Table('matches', metadata,
        Column('match_id', String(500), primary_key=True),
        Column('playername', String(500)),
        Column('playercolor', String(5)),
        Column('AIcolor', String(5)),
        Column('moves', ARRAY(String)),
        Column('winner', String(500)),
        Column('played', String(500)),
        Column('time', String(500))
    )

    ins = matches.insert().values(match_id=str(uuid.uuid4()),playername=pn, playercolor=pc, AIcolor=aic, moves=mov, winner=win, played=plyd, time=tim)

    conn = engine.connect()
    conn.execute(ins)

# dbpush('Aidan','White','Black',['white pawn from a2 to a4','black knight from b7 to d6'],'player','2021-05-10 5:31PM','180')
# dbpush('Aidan','Black','White',['white pawn from a2 to a4','black knight from b7 to d6'],'AI','2021-05-11 8:43PM','360')