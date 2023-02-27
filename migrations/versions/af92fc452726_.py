"""empty message

Revision ID: af92fc452726
Revises: 
Create Date: 2023-02-24 12:27:02.701777

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af92fc452726'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allergies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('allergie', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('biometrics',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('gender', sa.Float(), nullable=True),
    sa.Column('waist', sa.Float(), nullable=True),
    sa.Column('chest', sa.Float(), nullable=True),
    sa.Column('hip', sa.Float(), nullable=True),
    sa.Column('bim', sa.Float(), nullable=True),
    sa.Column('body_fat', sa.Float(), nullable=True),
    sa.Column('fat_free_mass', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('disliked_foods',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('food', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('patients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=128), nullable=False),
    sa.Column('last_name', sa.String(length=128), nullable=False),
    sa.Column('phone_number', sa.String(length=128), nullable=False),
    sa.Column('email', sa.String(length=128), nullable=False),
    sa.Column('country', sa.String(length=128), nullable=True),
    sa.Column('state', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('goals',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=True),
    sa.Column('bmi', sa.Float(), nullable=True),
    sa.Column('body_fat', sa.Float(), nullable=True),
    sa.Column('fat_free_mass', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('patients_allergies',
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('allergie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['allergie_id'], ['allergies.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('patient_id', 'allergie_id')
    )
    op.create_table('patients_biometrics',
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('biometric_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['biometric_id'], ['biometrics.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('patient_id', 'biometric_id')
    )
    op.create_table('patients_disliked_foods',
    sa.Column('patient_id', sa.Integer(), nullable=False),
    sa.Column('disliked_food_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['disliked_food_id'], ['disliked_foods.id'], ),
    sa.ForeignKeyConstraint(['patient_id'], ['patients.id'], ),
    sa.PrimaryKeyConstraint('patient_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients_disliked_foods')
    op.drop_table('patients_biometrics')
    op.drop_table('patients_allergies')
    op.drop_table('goals')
    op.drop_table('patients')
    op.drop_table('users')
    op.drop_table('disliked_foods')
    op.drop_table('biometrics')
    op.drop_table('allergies')
    # ### end Alembic commands ###