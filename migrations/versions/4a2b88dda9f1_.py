"""empty message

Revision ID: 4a2b88dda9f1
Revises: aab0ea3f5624
Create Date: 2021-07-10 16:11:47.447269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a2b88dda9f1'
down_revision = 'aab0ea3f5624'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('detail', sa.Column('request_number', sa.String(length=10), nullable=False))
    op.add_column('short', sa.Column('request_number', sa.String(length=10), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('short', 'request_number')
    op.drop_column('detail', 'request_number')
    # ### end Alembic commands ###