"""empty message

Revision ID: 0e92274a9a18
Revises: 4a2b88dda9f1
Create Date: 2021-07-10 16:43:18.083613

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '0e92274a9a18'
down_revision = '4a2b88dda9f1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('detail')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('detail',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('number', sa.VARCHAR(length=15), autoincrement=False, nullable=False),
    sa.Column('alt_number', sa.VARCHAR(length=15), autoincrement=False, nullable=True),
    sa.Column('message', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.Column('timestamp', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('state', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('pincode', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('firm', sa.VARCHAR(length=80), autoincrement=False, nullable=True),
    sa.Column('ownership', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('vertical', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('services', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('request_number', sa.VARCHAR(length=10), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='detail_pkey')
    )
    # ### end Alembic commands ###