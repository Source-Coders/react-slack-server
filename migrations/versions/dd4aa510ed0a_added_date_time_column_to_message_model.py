"""Added date_time column to Message model.

Revision ID: dd4aa510ed0a
Revises: f7e61a377eb3
Create Date: 2020-05-30 14:21:33.472210

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4aa510ed0a'
down_revision = 'f7e61a377eb3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('messages', sa.Column('date_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('messages', 'date_time')
    # ### end Alembic commands ###
