from Data import id, roles
from discord import Member


class User:
    dis_id: int
    name: str
    roles: list
    member: Member
    task: int


    def __init__(self, ctx, bot):
        self.dis_id = ctx.author.id
        self.name = ctx.author.name
        self.guild = bot.get_guild(id.channel_id)
        self.member = self.guild.get_member(ctx.author.id)
        self.roles = self.member.roles


    def admin(self) -> bool:
        for my_role in self.member.roles:
            if roles.role_cx3.get(5) == int(my_role.id):
                return True
        return False

    def role(self, *args):
        return self.guild.get_role(roles.role_cx3.get(args[0]))

    def language(self, *args):
        return self.guild.get_role(roles.language.get(args[0]))

    def get_roles(self):
        return self.member.get_roles

    def get_member(self):
        return self.member

    def get_guild(self):
        return self.guild
