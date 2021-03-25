"""empty message

Revision ID: 0d9e98b530de
Revises: 
Create Date: 2019-06-17 14:17:37.614943

"""
from alembic import op
import sqlalchemy as sa
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '0d9e98b530de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=True),
    sa.Column('desc', sa.String(length=120), nullable=True),
    sa.Column('thumbnail', flask_appbuilder.models.mixins.ImageColumn(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('discount', sa.Integer(), nullable=True),
    sa.Column('tag', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('sold', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_product_desc'), 'product', ['desc'], unique=False)
    op.create_index(op.f('ix_product_discount'), 'product', ['discount'], unique=False)
    op.create_index(op.f('ix_product_name'), 'product', ['name'], unique=False)
    op.create_index(op.f('ix_product_price'), 'product', ['price'], unique=False)
    op.create_index(op.f('ix_product_sold'), 'product', ['sold'], unique=False)
    op.create_index(op.f('ix_product_tag'), 'product', ['tag'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=False)
    op.create_table('product_image',
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('image', flask_appbuilder.models.mixins.ImageColumn(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('product_image')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_product_tag'), table_name='product')
    op.drop_index(op.f('ix_product_sold'), table_name='product')
    op.drop_index(op.f('ix_product_price'), table_name='product')
    op.drop_index(op.f('ix_product_name'), table_name='product')
    op.drop_index(op.f('ix_product_discount'), table_name='product')
    op.drop_index(op.f('ix_product_desc'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###