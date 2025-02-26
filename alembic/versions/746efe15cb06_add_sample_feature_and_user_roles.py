"""add_sample_feature_and_user_roles

Revision ID: 746efe15cb06
Revises: 
Create Date: 2025-02-26 10:15:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '746efe15cb06'
down_revision: Union[str, None] = None  # This is the base revision
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # This is just a placeholder since the tables already exist
    pass


def downgrade() -> None:
    # This is just a placeholder
    pass 