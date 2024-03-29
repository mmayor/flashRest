"""empty message

Revision ID: 2b54b23dec03
Revises: de8d1488ff93
Create Date: 2019-09-04 00:11:21.771179

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b54b23dec03'
down_revision = 'de8d1488ff93'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('address', table_name='contacts')
    op.drop_index('agenda_slug', table_name='contacts')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('agenda_slug', 'contacts', ['agenda_slug'], unique=True)
    op.create_index('address', 'contacts', ['address'], unique=True)
    # ### end Alembic commands ###
