from sqlalchemy import Column, BigInteger, UnicodeText, TIMESTAMP, Boolean
from sqlalchemy import func, text as satext

from .base import Base


class Message(Base):
    __tablename__ = 'messages'

    id = Column('id', BigInteger, primary_key=True)
    text = Column('text', UnicodeText, nullable=False)
    image = Column('image', UnicodeText)
    url = Column('url', UnicodeText, nullable=False)
    is_sent = Column('is_sent', Boolean, nullable=False, server_default='0')
    created_at = Column('created_at', TIMESTAMP, server_default=func.now())
    updated_at = Column('updated_at', TIMESTAMP,
                        server_default=satext('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    # @todo: tmp
    def __repr__(self):
        return '<Message id="%s" is_send="%s">' % (self.id, self.is_sent)
