"""categorias model

Revision ID: 9dd1a886c246
Revises: ca5539e5eb32
Create Date: 2023-01-21 19:54:30.356102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dd1a886c246'
down_revision = 'ca5539e5eb32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nombre', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('prodcutos', schema=None) as batch_op:
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=45),
               nullable=False)
        batch_op.alter_column('precio',
               existing_type=sa.FLOAT(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('prodcutos', schema=None) as batch_op:
        batch_op.alter_column('precio',
               existing_type=sa.FLOAT(),
               nullable=True)
        batch_op.alter_column('nombre',
               existing_type=sa.VARCHAR(length=45),
               nullable=True)

    op.drop_table('categorias')
    # ### end Alembic commands ###