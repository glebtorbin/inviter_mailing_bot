"""db

Revision ID: d46dc74b238c
Revises: 
Create Date: 2023-03-16 11:06:51.070848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd46dc74b238c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel_client',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('client_id', sa.String(length=100), nullable=False),
    sa.Column('ch_id_name', sa.String(length=100), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('status_invite', sa.Integer(), nullable=False),
    sa.Column('success_inv', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    comment='Таблица для хранения чатов и каналов клиента, куда инвайтить'
    )
    op.create_table('client_proxy_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Статус прокси на аккаунте'
    )
    op.create_table('client_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Статус аккаунта'
    )
    op.create_table('client_workes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Чем занят аккаунт'
    )
    op.create_table('keyword',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tag', sa.String(length=255), nullable=False, comment='тег'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tag')
    )
    op.create_table('members',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=500), nullable=True),
    sa.Column('last_name', sa.String(length=500), nullable=True),
    sa.Column('username', sa.String(length=500), nullable=True),
    sa.Column('invite_restricted', sa.Boolean(), nullable=True, comment='Заблокирован ли у юзера приём инвайтов (1 - да)'),
    sa.Column('source', sa.String(length=500), nullable=True, comment='Откуда участник'),
    sa.Column('chat_id', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=255), nullable=True),
    sa.Column('WA', sa.Boolean(), nullable=True, comment='есть ли у юзера Whatsapp'),
    sa.Column('client_id', sa.String(length=50), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    comment='Спарсенные участники групп'
    )
    op.create_table('plan_status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Статус плана'
    )
    op.create_table('proxy',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('proxy', sa.String(length=100), nullable=False),
    sa.Column('valid', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    comment='Все прокси'
    )
    op.create_table('reports',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('date', sa.String(length=50), nullable=False),
    sa.Column('ban_acc', sa.Integer(), nullable=True),
    sa.Column('ban_proxy', sa.Integer(), nullable=True),
    sa.Column('ban_groups', sa.Integer(), nullable=True),
    sa.Column('count_tg', sa.Integer(), nullable=True),
    sa.Column('count_wa', sa.Integer(), nullable=True),
    sa.Column('count_tel', sa.Integer(), nullable=True),
    sa.Column('count_email', sa.Integer(), nullable=True),
    sa.Column('new_users', sa.Integer(), nullable=True),
    sa.Column('new_orders', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date'),
    comment='Отчеты по работе'
    )
    op.create_table('system_status',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Статус системы'
    )
    op.create_table('user_role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Роль юзера'
    )
    op.create_table('wa_client_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Статус аккаунта WA'
    )
    op.create_table('wa_client_workes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='Чем занят аккаунт WA'
    )
    op.create_table('wa_mailing_statuses',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    comment='статус wa рассылки'
    )
    op.create_table('channels',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('title', sa.String(length=400), nullable=True, comment='название'),
    sa.Column('access_hash', sa.String(length=255), nullable=True, comment='access_hash'),
    sa.Column('username', sa.String(length=255), nullable=True, comment='username'),
    sa.Column('participants_count', sa.Integer(), nullable=True, comment='кол-во участников'),
    sa.Column('audience', sa.String(length=255), nullable=True, comment='аудитория'),
    sa.Column('keyword_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False, comment='время создания канала в бд'),
    sa.ForeignKeyConstraint(['keyword_id'], ['keyword.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('plans',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('date', sa.String(length=50), nullable=False),
    sa.Column('system_status', sa.Integer(), nullable=True),
    sa.Column('active_acc', sa.Integer(), nullable=True),
    sa.Column('active_proxy', sa.Integer(), nullable=True),
    sa.Column('active_users', sa.Integer(), nullable=True),
    sa.Column('active_groups', sa.Integer(), nullable=True),
    sa.Column('plan_inv', sa.Integer(), nullable=True),
    sa.Column('status_plan', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_plan'], ['plan_status.id'], ),
    sa.ForeignKeyConstraint(['system_status'], ['system_status.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('date'),
    comment='Отчеты по планам'
    )
    op.create_table('users',
    sa.Column('id', sa.String(length=20), nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('sphere', sa.String(length=150), nullable=True),
    sa.Column('job_title', sa.String(length=150), nullable=True),
    sa.Column('bot_usage', sa.String(length=150), nullable=True),
    sa.Column('where_from', sa.String(length=150), nullable=True),
    sa.Column('balance', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['user_role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Юзеры'
    )
    op.create_table('wa_client_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('id_instance', sa.String(length=100), nullable=False),
    sa.Column('api_token', sa.String(length=200), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=True),
    sa.Column('count_check', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['status_id'], ['wa_client_statuses.id'], ),
    sa.ForeignKeyConstraint(['work_id'], ['wa_client_workes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Аккаунты whatsapp'
    )
    op.create_table('channel_source',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_channel', sa.Integer(), nullable=False),
    sa.Column('id_source', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['id_channel'], ['channel_client.id'], ),
    sa.ForeignKeyConstraint(['id_source'], ['channels.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Таблица для хранения чатов источников'
    )
    op.create_table('client_accounts',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('work_id', sa.Integer(), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('proxy_id', sa.Integer(), nullable=True),
    sa.Column('proxy_status_id', sa.Integer(), nullable=False),
    sa.Column('api_id', sa.Integer(), nullable=False),
    sa.Column('api_hash', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=16), nullable=False),
    sa.Column('count_invite', sa.Integer(), nullable=True),
    sa.Column('data_paused', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.String(length=50), nullable=True),
    sa.Column('channel_id', sa.BigInteger(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['proxy_id'], ['proxy.id'], ),
    sa.ForeignKeyConstraint(['proxy_status_id'], ['client_proxy_statuses.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['client_statuses.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['work_id'], ['client_workes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='Аккаунты парсеры'
    )
    op.create_table('nps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service', sa.String(length=100), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('username', sa.String(length=500), nullable=True),
    sa.Column('mark', sa.String(length=5), nullable=False),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='nps клиентов'
    )
    op.create_table('search',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('keywords', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_bad_words',
    sa.Column('group_id', sa.String(length=40), nullable=False),
    sa.Column('user_id', sa.String(length=20), nullable=False),
    sa.Column('words', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('group_id'),
    comment='слова триггеры для антиспама юзера'
    )
    op.create_table('wa_mailing',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('creator', sa.String(length=20), nullable=False),
    sa.Column('status_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=True),
    sa.Column('send', sa.Integer(), nullable=False, comment='сколько сообщений отправлено'),
    sa.Column('for_sending', sa.Integer(), nullable=False, comment='сколько надо отправить'),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['creator'], ['users.id'], ),
    sa.ForeignKeyConstraint(['status_id'], ['wa_mailing_statuses.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='рассылки whatsapp'
    )
    op.create_table('search_chats',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('search_id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.BigInteger(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['search_id'], ['search.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wa_mailing_phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mailing_id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=50), nullable=False),
    sa.Column('is_send', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['mailing_id'], ['wa_mailing.id'], ),
    sa.PrimaryKeyConstraint('id'),
    comment='номера для рассылок'
    )
    op.execute("INSERT INTO client_proxy_statuses VALUES (3,'Error'),(4,'None'),(2,'OFF'),(1,'ON')")
    op.execute("INSERT INTO client_statuses VALUES (1,'authorized'),(3,'banned'),(4,'paused'),(2,'waiting_for_authorization'),(5,'reserve')")
    op.execute("INSERT INTO client_workes VALUES (2,'inviting'),(4,'mailing'),(3,'parsing'),(1,'unworking')")
    op.execute("INSERT INTO user_role VALUES (10,'admin'),(5,'pending'),(2, 'user')")
    op.execute("INSERT INTO wa_client_statuses VALUES (1,'authorized'),(3,'banned'),(2,'waiting_for_authorization')")
    op.execute("INSERT INTO wa_client_workes VALUES (2,'checking'),(1,'unworking')")
    op.execute("INSERT INTO reports VALUES (1, 0, 0, 0 ,0, 0, 0, 0, 0, 0, 0)")
    op.execute("INSERT INTO wa_mailing_statuses VALUES (1,'unworking'),(2,'working'),(3,'finished'),(4,'paused')")


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wa_mailing_phones')
    op.drop_table('search_chats')
    op.drop_table('wa_mailing')
    op.drop_table('user_bad_words')
    op.drop_table('search')
    op.drop_table('nps')
    op.drop_table('client_accounts')
    op.drop_table('channel_source')
    op.drop_table('wa_client_accounts')
    op.drop_table('users')
    op.drop_table('plans')
    op.drop_table('channels')
    op.drop_table('wa_mailing_statuses')
    op.drop_table('wa_client_workes')
    op.drop_table('wa_client_statuses')
    op.drop_table('user_role')
    op.drop_table('system_status')
    op.drop_table('reports')
    op.drop_table('proxy')
    op.drop_table('plan_status')
    op.drop_table('members')
    op.drop_table('keyword')
    op.drop_table('client_workes')
    op.drop_table('client_statuses')
    op.drop_table('client_proxy_statuses')
    op.drop_table('channel_client')
    # ### end Alembic commands ###
