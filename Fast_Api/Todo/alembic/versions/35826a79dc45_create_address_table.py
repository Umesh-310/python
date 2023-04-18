"""create address table

Revision ID: 35826a79dc45
Revises: 31419831951f
Create Date: 2023-04-14 12:26:11.082055

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35826a79dc45'
down_revision = '31419831951f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('address',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('address1', sa.String(255), nullable=False),
                    sa.Column('address2', sa.String(255), nullable=False),
                    sa.Column('city', sa.String(45), nullable=False),
                    sa.Column('state', sa.String(45), nullable=False),
                    sa.Column('country', sa.String(45), nullable=False),
                    sa.Column('pincode', sa.String(45), nullable=False),
                    )

def downgrade() -> None:
    pass
