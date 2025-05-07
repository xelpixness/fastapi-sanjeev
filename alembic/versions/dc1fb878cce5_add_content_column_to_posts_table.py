"""add content column to posts table

Revision ID: dc1fb878cce5
Revises: b0c6bc417953
Create Date: 2025-05-04 17:25:13.865737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc1fb878cce5'
down_revision: Union[str, None] = 'b0c6bc417953'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))

def downgrade() -> None:
    op.drop_column('posts', 'content')