""""cpu_ram_for_failover"

Revision ID: 7b30bd0800c2
Revises: 8f454f913981
Create Date: 2017-10-11 14:27:41.703553

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b30bd0800c2'
down_revision = 'b08a738a829f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('failover', sa.Column('cpu', sa.Integer(), nullable=True))
    op.add_column('failover', sa.Column('ram', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('failover', 'ram')
    op.drop_column('failover', 'cpu')
    # ### end Alembic commands ###