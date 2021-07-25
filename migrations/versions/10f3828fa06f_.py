"""empty message

Revision ID: 10f3828fa06f
Revises: 44be47f197f8
Create Date: 2021-07-10 15:52:26.865721

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '10f3828fa06f'
down_revision = '44be47f197f8'
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
    sa.Column('number', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('alt_number', sa.INTEGER(), autoincrement=False, nullable=True),
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
    sa.PrimaryKeyConstraint('id', name='detail_pkey')
    )
    # ### end Alembic commands ###