"""empty message

Revision ID: 1246c59369b7
Revises: 
Create Date: 2020-11-10 23:41:14.248963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1246c59369b7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actions',
    sa.Column('action_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('action_id')
    )
    op.create_table('orgs',
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('org_id')
    )
    op.create_table('resources',
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('resource_id')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('role_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('channels',
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('is_private', sa.Boolean(), nullable=True),
    sa.Column('admin_username', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['admin_username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('channel_id')
    )
    op.create_table('messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('sent_dt', sa.DateTime(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['sender_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('org_invites',
    sa.Column('invite_id', sa.Integer(), nullable=False),
    sa.Column('inviter_id', sa.Integer(), nullable=True),
    sa.Column('org_id', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('responded', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['inviter_id'], ['users.user_id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['orgs.org_id'], ),
    sa.PrimaryKeyConstraint('invite_id')
    )
    op.create_table('org_members',
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['org_id'], ['orgs.org_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('org_id', 'user_id', 'role_id')
    )
    op.create_table('permissions',
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=True),
    sa.Column('action_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['action_id'], ['actions.action_id'], ),
    sa.ForeignKeyConstraint(['resource_id'], ['resources.resource_id'], ),
    sa.PrimaryKeyConstraint('permission_id')
    )
    op.create_table('channel_members',
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.channel_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('channel_id', 'user_id', 'role_id')
    )
    op.create_table('channel_messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.channel_id'], ),
    sa.ForeignKeyConstraint(['message_id'], ['messages.message_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('org_channels',
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.channel_id'], ),
    sa.ForeignKeyConstraint(['org_id'], ['orgs.org_id'], ),
    sa.PrimaryKeyConstraint('org_id', 'channel_id')
    )
    op.create_table('private_messages',
    sa.Column('message_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['message_id'], ['messages.message_id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('message_id')
    )
    op.create_table('role_permissions',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('permission_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['permissions.permission_id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['roles.role_id'], ),
    sa.PrimaryKeyConstraint('role_id', 'permission_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_permissions')
    op.drop_table('private_messages')
    op.drop_table('org_channels')
    op.drop_table('channel_messages')
    op.drop_table('channel_members')
    op.drop_table('permissions')
    op.drop_table('org_members')
    op.drop_table('org_invites')
    op.drop_table('messages')
    op.drop_table('channels')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
    op.drop_table('resources')
    op.drop_table('orgs')
    op.drop_table('actions')
    # ### end Alembic commands ###
