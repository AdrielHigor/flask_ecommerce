"""empty message

Revision ID: 67bdf0fc8fb5
Revises: bcf49fddaca4
Create Date: 2019-06-14 21:29:22.818135

"""
from alembic import op
import sqlalchemy as sa
import flask_appbuilder

# revision identifiers, used by Alembic.
revision = '67bdf0fc8fb5'
down_revision = 'bcf49fddaca4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('desc', sa.String(length=120), nullable=True))
    op.add_column('product', sa.Column('name', sa.String(length=120), nullable=True))
    op.add_column('product', sa.Column('thumbnail', flask_appbuilder.models.mixins.ImageColumn(), nullable=True))
    op.create_index(op.f('ix_product_desc'), 'product', ['desc'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=False)
    op.drop_index('ix_product_product_desc', table_name='product')
    op.drop_index('ix_product_product_name', table_name='product')
    op.create_unique_constraint(None, 'product', ['id'])
    op.drop_column('product', 'product_desc')
    op.drop_column('product', 'product_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('product_name', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('product_desc', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'product', type_='unique')
    op.create_index('ix_product_product_name', 'product', ['product_name'], unique=False)
    op.create_index('ix_product_product_desc', 'product', ['product_desc'], unique=False)
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_desc'), table_name='product')
    op.drop_column('product', 'thumbnail')
    op.drop_column('product', 'name')
    op.drop_column('product', 'desc')
    # ### end Alembic commands ###
