#DO NOT RUN

from sqlalchemy import Table, Column, String, MetaData, create_engine, ARRAY
import uuid
import os
import re

def dbpush(pn,pc,aic,mov,win,plyd):

    engine = create_engine("postgresql://iuulkwuvvrdmxw:b53508be72378dc1e867c7b4155e7dab99eaf2ee92a4c5c18cb62bffbb6a0342@ec2-35-174-35-242.compute-1.amazonaws.com:5432/d4m4h0c2mu2o1u", echo=True)
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