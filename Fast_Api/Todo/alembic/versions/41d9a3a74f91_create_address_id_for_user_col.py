"""create address id for user col

Revision ID: 41d9a3a74f91
Revises: 35826a79dc45
Create Date: 2023-04-14 12:38:22.542379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '41d9a3a74f91'
down_revision = '35826a79dc45'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column(
        'address_id', sa.Integer(), nullable=True))
    op.create_foreign_key('address_users_fk', source_table="users",
                          referent_table="address", local_cols=['address_id'], remote_cols=['id'], ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint('address_users_fk', table_name="users")
    op.drop_column('users', 'adress_id')
