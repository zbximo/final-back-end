# coding: utf-8
from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.mysql import TEXT, VARCHAR
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class TbInfoApp(Base):
    __tablename__ = 'tb_info_app'
    __table_args__ = {'comment': '应用表，包含微信、QQ、推特、电话等'}

    id = Column(Integer, primary_key=True)
    app_name = Column(VARCHAR(255))
    create_datetime = Column(DateTime, nullable=False)


class TbInfoUser(Base):
    __tablename__ = 'tb_info_user'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255))
    card_id = Column(VARCHAR(255), nullable=False)
    birthday = Column(Date)
    sex = Column(VARCHAR(255))
    address = Column(String(255, 'utf8mb4_bin'), comment='户籍地')
    arrested = Column(String(255, 'utf8mb4_bin'), comment='是否被抓捕')
    score = Column(Float, comment='分数')
    create_datetime = Column(DateTime, nullable=False)


class TbSysUserPermission(Base):
    __tablename__ = 'tb_sys_user_permission'
    __table_args__ = {'comment': '用户权限表'}

    id = Column(Integer, primary_key=True)
    permission = Column(TEXT)
    create_datetime = Column(DateTime, nullable=False)


class TbDelivery(Base):
    __tablename__ = 'tb_delivery'
    __table_args__ = {'comment': '个人间快递信息'}

    id = Column(Integer, primary_key=True)
    from_user_id = Column(ForeignKey('tb_info_user.id'), nullable=False, index=True)
    to_user_id = Column(ForeignKey('tb_info_user.id'), nullable=False, index=True)
    from_address = Column(VARCHAR(255))
    to_address = Column(VARCHAR(255))
    record_datetime = Column(DateTime)
    create_datetime = Column(DateTime, nullable=False)

    from_user = relationship('TbInfoUser', primaryjoin='TbDelivery.from_user_id == TbInfoUser.id')
    to_user = relationship('TbInfoUser', primaryjoin='TbDelivery.to_user_id == TbInfoUser.id')


class TbInfoAppUser(Base):
    __tablename__ = 'tb_info_app_user'
    __table_args__ = {'comment': '由app_id和user_id组合，保存app_user_id，即APP用户账号。'}

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('tb_info_user.id'), nullable=False, index=True)
    app_id = Column(ForeignKey('tb_info_app.id'), nullable=False, index=True)
    app_user_account = Column(VARCHAR(255), nullable=False)
    app_user_nickname = Column(VARCHAR(255))
    create_datetime = Column(DateTime, nullable=False)

    app = relationship('TbInfoApp')
    user = relationship('TbInfoUser')


class TbInfoGroup(Base):
    __tablename__ = 'tb_info_group'

    id = Column(Integer, primary_key=True)
    group_id = Column(VARCHAR(255), nullable=False)
    group_name = Column(VARCHAR(255), nullable=False)
    app_id = Column(ForeignKey('tb_info_app.id'), nullable=False, index=True)
    create_datetime = Column(DateTime, nullable=False)

    app = relationship('TbInfoApp')


class TbInfoTelephone(Base):
    __tablename__ = 'tb_info_telephone'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('tb_info_user.id'), nullable=False, index=True)
    telephone = Column(VARCHAR(255), nullable=False)
    create_datetime = Column(DateTime, nullable=False)

    user = relationship('TbInfoUser')


class TbSysUser(Base):
    __tablename__ = 'tb_sys_user'
    __table_args__ = {'comment': '系统用户信息'}

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(VARCHAR(255))
    pwd = Column(VARCHAR(255))
    account = Column(Integer, primary_key=True, nullable=False)
    permission_id = Column(ForeignKey('tb_sys_user_permission.id'), index=True)
    create_datetime = Column(DateTime, nullable=False)

    permission = relationship('TbSysUserPermission')


class TbContentPersonal(Base):
    __tablename__ = 'tb_content_personal'
    __table_args__ = {'comment': '个人间不同应用的聊天记录、购物记录'}

    id = Column(Integer, primary_key=True)
    from_app_user_id = Column(ForeignKey('tb_info_app_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    to_app_user_id = Column(ForeignKey('tb_info_app_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), nullable=False, index=True)
    keywords = Column(VARCHAR(255))
    content = Column(TEXT)
    record_datetime = Column(DateTime)
    create_datetime = Column(DateTime, nullable=False)

    from_app_user = relationship('TbInfoAppUser', primaryjoin='TbContentPersonal.from_app_user_id == TbInfoAppUser.id')
    to_app_user = relationship('TbInfoAppUser', primaryjoin='TbContentPersonal.to_app_user_id == TbInfoAppUser.id')


class TbInfoGroupUser(Base):
    __tablename__ = 'tb_info_group_user'
    __table_args__ = {'comment': '用户和群'}

    id = Column(Integer, primary_key=True)
    app_user_id = Column(ForeignKey('tb_info_app_user.id'), nullable=False, index=True)
    group_id = Column(ForeignKey('tb_info_group.id'), nullable=False, index=True)
    create_datetime = Column(DateTime, nullable=False)

    app_user = relationship('TbInfoAppUser')
    group = relationship('TbInfoGroup')


class TbSearch(Base):
    __tablename__ = 'tb_search'
    __table_args__ = {'comment': '搜索记录'}

    id = Column(Integer, primary_key=True)
    app_user_id = Column(ForeignKey('tb_info_app_user.id'), nullable=False, index=True)
    keywords = Column(VARCHAR(255))
    content = Column(TEXT)
    record_datetime = Column(DateTime)
    create_datetime = Column(DateTime, nullable=False)

    app_user = relationship('TbInfoAppUser')


class TbTelephoneRecord(Base):
    __tablename__ = 'tb_telephone_record'
    __table_args__ = {'comment': '个人间电话记录'}

    id = Column(Integer, primary_key=True)
    from_telephone_id = Column(ForeignKey('tb_info_telephone.id'), nullable=False, index=True)
    to_telephone_id = Column(ForeignKey('tb_info_telephone.id'), nullable=False, index=True)
    record_datetime = Column(DateTime)
    create_datetime = Column(DateTime, nullable=False)

    from_telephone = relationship('TbInfoTelephone', primaryjoin='TbTelephoneRecord.from_telephone_id == TbInfoTelephone.id')
    to_telephone = relationship('TbInfoTelephone', primaryjoin='TbTelephoneRecord.to_telephone_id == TbInfoTelephone.id')


class TbContentGroupUser(Base):
    __tablename__ = 'tb_content_group_user'
    __table_args__ = {'comment': '存储组内用户发言'}

    id = Column(Integer, primary_key=True)
    group_user_id = Column(ForeignKey('tb_info_group_user.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    keywords = Column(VARCHAR(255))
    content = Column(TEXT)
    record_datetime = Column(DateTime)
    create_datetime = Column(DateTime, nullable=False)

    group_user = relationship('TbInfoGroupUser')
