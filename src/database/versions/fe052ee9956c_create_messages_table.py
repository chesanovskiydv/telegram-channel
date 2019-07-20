"""create messages table

Revision ID: fe052ee9956c
Revises: 
Create Date: 2019-07-18 22:04:10.886151

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'fe052ee9956c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'messages',
        sa.Column('id', sa.BigInteger, primary_key=True),
        sa.Column('text', sa.UnicodeText, nullable=False),
        sa.Column('image', sa.UnicodeText),
        sa.Column('url', sa.UnicodeText, nullable=False),
        sa.Column('is_sent', sa.Boolean, nullable=False, server_default='0'),
        sa.Column('created_at', sa.TIMESTAMP, server_default=sa.func.now()),
        sa.Column('updated_at', sa.TIMESTAMP, server_default=sa.text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    )


def downgrade():
    op.drop_table('messages')
