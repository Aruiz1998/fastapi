"""Add content to posts table

Revision ID: fb22c9eaa6ed
Revises: 42ff66b44c96
Create Date: 2024-10-13 06:38:29.245616

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb22c9eaa6ed'
down_revision: Union[str, None] = '42ff66b44c96'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('blog_posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('blog_posts', 'content')
    pass
