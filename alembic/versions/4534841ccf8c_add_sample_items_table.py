# Create a file named alembic/versions/4534841ccf8c_add_sample_items_table.py
"""add_sample_items_table

Revision ID: 4534841ccf8c
Revises: 746efe15cb06
Create Date: 2025-02-26 10:17:31.836617

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4534841ccf8c'
down_revision: Union[str, None] = '746efe15cb06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # This is just a placeholder since the tables already exist
    pass


def downgrade() -> None:
    pass
