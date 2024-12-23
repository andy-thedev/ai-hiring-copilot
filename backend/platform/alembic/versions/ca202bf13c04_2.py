"""“2”

Revision ID: ca202bf13c04
Revises: bdd2c2ec70eb
Create Date: 2024-11-18 09:49:50.180716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'ca202bf13c04'
down_revision: Union[str, None] = 'bdd2c2ec70eb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('resume', sa.Column('role_id', sa.String(), nullable=True))
    op.alter_column('resume', 'role',
               existing_type=postgresql.ENUM('SENIOR_PRODUCT_ENGINEER', name='roletypes'),
               nullable=True)
    op.create_foreign_key(None, 'resume', 'role', ['role_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'resume', type_='foreignkey')
    op.alter_column('resume', 'role',
               existing_type=postgresql.ENUM('SENIOR_PRODUCT_ENGINEER', name='roletypes'),
               nullable=False)
    op.drop_column('resume', 'role_id')
    op.drop_table('role')
    # ### end Alembic commands ###
