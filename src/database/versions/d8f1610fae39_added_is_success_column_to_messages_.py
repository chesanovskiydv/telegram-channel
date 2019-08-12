"""Added 'is_success' column to 'messages' table

Revision ID: d8f1610fae39
Revises: fe052ee9956c
Create Date: 2019-08-12 11:19:45.417616

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd8f1610fae39'
down_revision = 'fe052ee9956c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('messages', sa.Column('is_success', sa.Boolean, nullable=True))


def downgrade():
    op.drop_column('messages', 'is_success')
