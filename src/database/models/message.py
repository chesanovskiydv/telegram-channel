from sqlalchemy import Column, BigInteger, UnicodeText, String, TIMESTAMP, Boolean
from sqlalchemy import func, text as satext

from .base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column('id', BigInteger, primary_key=True)
    text = Column('text', UnicodeText)
    image = Column('image', String(64), nullable=True)
    url = Column('url', UnicodeText)
    is_sent = Column('is_sent', Boolean, server_default='0')
    created_at = Column('created_at', TIMESTAMP, server_default=func.now())
    updated_at = Column('updated_at', TIMESTAMP,
                        server_default=satext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
