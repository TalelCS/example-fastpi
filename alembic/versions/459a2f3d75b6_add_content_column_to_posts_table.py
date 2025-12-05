"""add content column to posts table

Revision ID: 459a2f3d75b6
Revises: d4e482e4539e
Create Date: 2025-12-05 14:54:39.924507

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '459a2f3d75b6'
down_revision: Union[str, Sequence[str], None] = 'd4e482e4539e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts', 'content')
    pass
