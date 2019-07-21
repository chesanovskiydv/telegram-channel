# -*- coding: utf-8 -*-
from sqlalchemy import Column, BigInteger, UnicodeText, TIMESTAMP
from sqlalchemy import func, text as satext

from .base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column(BigInteger, primary_key=True)
    text = Column(UnicodeText, nullable=False)
    image = Column(UnicodeText)
    url = Column(UnicodeText, nullable=False)
    sent_at = Column(TIMESTAMP, nullable=True, server_default=None)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=satext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
