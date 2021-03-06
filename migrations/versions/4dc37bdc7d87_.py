"""empty message

Revision ID: 4dc37bdc7d87
Revises: 
Create Date: 2021-03-05 13:02:06.496291

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dc37bdc7d87'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('complete', sa.Boolean(), nullable=False))
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('todos', 'complete')
    # ### end Alembic commands ###
