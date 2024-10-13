"""Add final columns to post table

Revision ID: 05f2f18bed05
Revises: 37bf4434c791
Create Date: 2024-10-13 06:55:37.497405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '05f2f18bed05'
down_revision: Union[str, None] = '37bf4434c791'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('blog_posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('blog_posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('blog_posts', 'published')
    op.drop_column('blog_posts', 'created_at')
    pass
