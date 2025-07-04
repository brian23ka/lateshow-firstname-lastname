"""initial

Revision ID: 3d1cc180c578
Revises: 
Create Date: 2025-06-22 10:39:33.238865

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d1cc180c578'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('episode',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('number', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('guest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('occupation', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('appearance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('guest_id', sa.Integer(), nullable=True),
    sa.Column('episode_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['episode_id'], ['episode.id'], ),
    sa.ForeignKeyConstraint(['guest_id'], ['guest.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('appearance')
    op.drop_table('guest')
    op.drop_table('episode')
    # ### end Alembic commands ###
