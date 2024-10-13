"""Add foreign key to posts table

Revision ID: 37bf4434c791
Revises: 3c6b7f30f3b9
Create Date: 2024-10-13 06:50:19.495141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '37bf4434c791'
down_revision: Union[str, None] = '3c6b7f30f3b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('blog_posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table='blog_posts', referent_table='users', 
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='blog_posts')
    op.drop_column('blog_posts', 'owner_id')
    pass
