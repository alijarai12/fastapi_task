"""second migrations

Revision ID: f4d39d92ac28
Revises: f6fa6b16e1d3
Create Date: 2023-12-21 12:03:04.671550

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f4d39d92ac28'
down_revision: Union[str, None] = 'f6fa6b16e1d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
