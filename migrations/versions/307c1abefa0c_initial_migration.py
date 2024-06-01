"""Initial migration.

Revision ID: 307c1abefa0c
Revises: 
Create Date: 2024-06-01 12:23:38.425647

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307c1abefa0c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=60), nullable=False),
    sa.Column('is_lecturer', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_text', sa.Text(), nullable=False),
    sa.Column('answer_key', sa.Text(), nullable=False),
    sa.Column('lecturer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['lecturer_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('answer_text', sa.Text(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('submitted_at', sa.DateTime(), nullable=False),
    sa.Column('grade', sa.Float(), nullable=True),
    sa.Column('is_graded', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('test_attempt',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('attempted_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['student_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test_attempt')
    op.drop_table('answer')
    op.drop_table('question')
    op.drop_table('user')
    # ### end Alembic commands ###
