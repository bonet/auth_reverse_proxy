"""empty message

Revision ID: cdfbef659b69
Revises: 
Create Date: 2022-01-26 01:44:26.083539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdfbef659b69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    users_table = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('password', sa.LargeBinary(length=128), nullable=True),
    sa.Column('fullname', sa.String(length=256), nullable=True),
    sa.Column('address', sa.String(length=256), nullable=True),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )

    op.bulk_insert(users_table,
    [
        {'id':1, 'email':'111@test.com', 'password':'123456'.encode('ascii') },
        {'id':2, 'email':'222@test.com', 'password':'123456'.encode('ascii') },
        {'id':3, 'email':'333@test.com', 'password':'123456'.encode('ascii') }
    ]
)


def downgrade():
    op.drop_table('users')
