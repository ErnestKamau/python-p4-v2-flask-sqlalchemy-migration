"""rename department

Revision ID: 16fb0f4bdb20
Revises: 1209d5a5559e
Create Date: 2025-06-13 01:43:18.615568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16fb0f4bdb20'
down_revision = '1209d5a5559e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
