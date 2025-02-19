"""initial_migration

Revision ID: 1eb8ad12f5a0
Revises: 
Create Date: 2022-08-31 12:28:50.754314

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1eb8ad12f5a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vlp',
    sa.Column('well_id', sa.String(), nullable=False, comment='Дебиты жидкости, м3/сут'),
    sa.Column('vlp', sa.String(), nullable=False, comment='Забойное давление, атм'),
    sa.PrimaryKeyConstraint('well_id')
    )
    op.create_table('well_data',
    sa.Column('id', sa.String(), nullable=False, comment='Идентификатор набора входных данных'),
    sa.Column('inclinometry', sa.String(), nullable=False, comment='Инклинометрия'),
    sa.Column('d_cas', sa.Float(), nullable=False, comment='Данные по ЭК'),
    sa.Column('h_tub', sa.Float(), nullable=False, comment='Глубина спуска НКТ, м'),
    sa.Column('d_tub', sa.Float(), nullable=False, comment='Данные по НКТ'),
    sa.Column('wct', sa.Float(), nullable=False, comment='Обводненность, %'),
    sa.Column('rp', sa.Float(), nullable=False, comment='Газовый фактор, м3/т'),
    sa.Column('gamma_oil', sa.Float(), nullable=False, comment='Отн. плотность нефти'),
    sa.Column('gamma_gas', sa.Float(), nullable=False, comment='Отн. плотность газа'),
    sa.Column('gamma_wat', sa.Float(), nullable=False, comment='Отн. плотность воды'),
    sa.Column('t_res', sa.Float(), nullable=False, comment='Пластовая температура, C'),
    sa.Column('p_wh', sa.Float(), nullable=False, comment='Буферное давление, атм'),
    sa.Column('geo_grad', sa.Float(), nullable=False, comment='Градиент температуры, C/100 м'),
    sa.Column('h_res', sa.Float(), nullable=False, comment='Глубина Верхних Дыр Перфорации, м'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('well_data')
    op.drop_table('vlp')
    # ### end Alembic commands ###
