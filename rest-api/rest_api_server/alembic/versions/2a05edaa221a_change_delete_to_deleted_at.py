""""“change_delete_to_deleted_at”"

Revision ID: 2a05edaa221a
Revises: eb2dc922a243
Create Date: 2017-06-15 10:44:37.424859

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.sql import table, column
from sqlalchemy import update, String
from datetime import datetime

# revision identifiers, used by Alembic.
revision = '2a05edaa221a'
down_revision = 'eb2dc922a243'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    try:
        for table_name in ['agent', 'backup', 'cloudsite', 'customer',
                           'device',
                           'drive', 'drplan', 'failover', 'group', 'partner',
                           'snapshot', 'vsphere_credential']:
            op.add_column(table_name, sa.Column(
                'deleted_at', sa.Integer(), nullable=False, default=0))
            entity_table = table(
                table_name, column('deleted', sa.Boolean()),
                column('deleted_at', sa.Integer()))
            upd_not_deleted = update(entity_table).values(
                deleted_at=0).where(entity_table.c.deleted.isnot(True))
            upd_deleted = update(entity_table).values(
                deleted_at=int(datetime.utcnow().timestamp())).where(
                entity_table.c.deleted.is_(True))
            session.execute(upd_deleted)
            session.execute(upd_not_deleted)
            op.drop_column(table_name, 'deleted')
        session.commit()
    finally:
        session.close()
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    session = Session(bind=bind)
    try:
        for table_name in ['agent', 'backup', 'cloudsite', 'customer',
                           'device',
                           'drive', 'drplan', 'failover', 'group', 'partner',
                           'snapshot', 'vsphere_credential']:
            op.add_column(table_name, sa.Column(
                'deleted', sa.Boolean(), default=False))
            entity_table = table(
                table_name, column('deleted', sa.Boolean()),
                column('deleted_at', sa.Integer()))
            upd_deleted = update(entity_table).values(
                deleted=True).where(entity_table.c.deleted_at != 0)
            upd_not_deleted = update(entity_table).values(
                deleted=False).where(entity_table.c.deleted_at == 0)
            session.execute(upd_deleted)
            session.execute(upd_not_deleted)
            op.drop_column(table_name, 'deleted_at')
        session.commit()
    finally:
        session.close()
    # ### end Alembic commands ###