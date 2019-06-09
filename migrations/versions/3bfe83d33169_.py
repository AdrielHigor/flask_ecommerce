"""empty message

Revision ID: 3bfe83d33169
Revises: f7ff2ef34328
Create Date: 2019-06-08 22:46:30.820721

"""
from alembic import op
import sqlalchemy as sa
import flask_appbuilder


# revision identifiers, used by Alembic.
revision = '3bfe83d33169'
down_revision = 'f7ff2ef34328'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product_name', sa.String(length=120), nullable=True),
    sa.Column('product_img', flask_appbuilder.models.mixins.ImageColumn(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_product_product_name'), 'product', ['product_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_product_product_name'), table_name='product')
    op.drop_table('product')
    # ### end Alembic commands ###