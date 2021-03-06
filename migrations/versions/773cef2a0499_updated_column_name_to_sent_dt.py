"""updated column name to sent_dt

Revision ID: 773cef2a0499
Revises: dd4aa510ed0a
Create Date: 2020-05-30 14:23:46.421474

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '773cef2a0499'
down_revision = 'dd4aa510ed0a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('sent_dt', sa.DateTime(), nullable=True))
    op.drop_column('messages', 'date_time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('date_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('messages', 'sent_dt')
    # ### end Alembic commands ###
