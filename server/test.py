# _*_ coding = utf-8 _*_

from model import Building, Stage, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///%s' % 'iamhere.db?charset=utf8', connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


## Добавим здание
# name = "ГО"
# description = "ул. Угличская, 36"
# building = Building(name, description)
# session.add(building)
# session.commit()
#
## Добавим этаж
# stage = Stage(building_id=1, name="1", image_id="1")
# session.add(stage)
# session.commit()
def create_building(name, descr):
    building = Building(name, descr)
    session.add(building)
    session.commit()


def create_stage(b_id, name, i_id):
    stage = Stage(building_id=b_id, name=name, image_id=i_id)
    session.add(stage)
    session.commit()


def delete_data():
    session.query(Stage).filter_by(building_id=1).delete()
    session.commit()
    for i in range(1, session.query(Building).count() + 1):
        session.query(Building).filter_by(id=i).delete()
    session.commit()


create_building("test", "уг 36")
for i in range(1, 8):
    create_stage(1, str(i), str(i))
