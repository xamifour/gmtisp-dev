from openwisp_users.apps import OpenwispUsersConfig


class GmtispUsersConfig(OpenwispUsersConfig):
    name = 'gmtisp.gmtisp_users'
    label = 'gmtisp_users'


del OpenwispUsersConfig
