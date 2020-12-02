"""initial migration

Revision ID: ebe2ddc3fc36
Revises: 
Create Date: 2020-12-02 12:28:27.460133

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ebe2ddc3fc36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('email', table_name='users_old')
    op.drop_index('email_2', table_name='users_old')
    op.drop_index('username', table_name='users_old')
    op.drop_index('username_2', table_name='users_old')
    op.drop_table('users_old')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_old',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('email', mysql.VARCHAR(collation='utf8_swedish_ci', length=64), nullable=False),
    sa.Column('username', mysql.VARCHAR(collation='utf8_swedish_ci', length=64), nullable=False),
    sa.Column('password_hash', mysql.VARCHAR(collation='utf8_swedish_ci', length=128), nullable=False),
    sa.Column('role_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('confirmed', mysql.TINYINT(display_width=1), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8_swedish_ci',
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('username_2', 'users_old', ['username'], unique=False)
    op.create_index('username', 'users_old', ['username'], unique=True)
    op.create_index('email_2', 'users_old', ['email'], unique=False)
    op.create_index('email', 'users_old', ['email'], unique=True)
    # ### end Alembic commands ###
