"""create phone number for user col

Revision ID: 31419831951f
Revises: 
Create Date: 2023-04-14 12:05:16.950228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31419831951f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column(
        "phone_number", sa.String(15), nullable=True))


def downgrade() -> None:
    # pass
    op.drop_column('users', 'phone_number')
    # this is delete column from the table
