"""empty message

Revision ID: 693de4410a10
Revises: 
Create Date: 2020-08-21 23:06:47.558595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693de4410a10'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('semesters',
    sa.Column('id', sa.Integer()),
    sa.PrimaryKeyConstraint('id'),
    )
    op.create_table('courses',
    sa.Column('id', sa.Integer()),
    sa.Column('course_id', sa.String(length=64)),
    sa.Column('course_title', sa.String(length=64)),
    sa.Column('description', sa.String(length=64)),
    sa.Column('vid_title1', sa.String(length=64)),
    sa.Column('vid_desc1', sa.String(length=64)),
    sa.Column('vid_title2', sa.String(length=64)),
    sa.Column('vid_desc2', sa.String(length=64)),
    sa.Column('resc_title1', sa.String(length=64)),
    sa.Column('resc_desc1', sa.String(length=64)),
    sa.Column('resc_title2', sa.String(length=64)),
    sa.Column('resc_desc2', sa.String(length=64)),
    sa.Column('resc_title3', sa.String(length=64)),
    sa.Column('resc_desc3', sa.String(length=64)),
    sa.Column('vid_link1', sa.String(length=64)),
    sa.Column('vid_link2', sa.String(length=64)),
    sa.Column('resc_link1', sa.String(length=64)),
    sa.Column('resc_link2', sa.String(length=64)),
    sa.Column('resc_link3', sa.String(length=64)),
    sa.Column('mit_link', sa.String(length=64)),

    sa.Column('semester_id', sa.Integer()),
    sa.ForeignKeyConstraint(['semester_id'], ['semesters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_courses_courseid', 'courses', ['course_id'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_courses_courseid', 'courses')
    op.drop_table('semesters')
    op.drop_table('courses')
    ### end Alembic commands ###