"""empty message

Revision ID: 0b75ef832bbd
Revises: 33d8c3c1f3dd
Create Date: 2024-09-25 21:35:54.947283

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b75ef832bbd'
down_revision = '33d8c3c1f3dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('county', sa.String(length=50), nullable=False))
        batch_op.drop_column('zip_code')
        batch_op.drop_column('state')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('addresses', schema=None) as batch_op:
        batch_op.add_column(sa.Column('state', sa.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('zip_code', sa.VARCHAR(length=10), nullable=False))
        batch_op.drop_column('county')

    # ### end Alembic commands ###
