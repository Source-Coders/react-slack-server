from .. import db, ma
from sqlalchemy import select
from sqlalchemy.orm import column_property
from .OrgMembers import org_members
from .User import User
from .RolePermissions import role_permissions
from .Permissions import permissions
from .Resource import Resource
from .Action import Action

role_permissions_alias = select([
    role_permissions.c.role_id.label("role_id_a"),
    role_permissions.c.permission_id
]).alias()

User_alias = select([
    User.user_id.label("user_id_a"),
    User.username,
    User.password_hash
]).alias()

permissions_alias = select([
    permissions.c.permission_id.label("permission_id_a"),
    permissions.c.resource_id,
    permissions.c.action_id
]).alias()

ResourceAlias = select([
    Resource.resource_id.label("resource_id_a"),
    Resource.name.label("name_a")
]).alias()

ActionAlias = select([
    Action.action_id.label("action_id_a"),
    Action.name.label("name")
]).alias()

org_member_permission_join = db.join(org_members, role_permissions_alias, org_members.c.role_id == role_permissions_alias.c.role_id_a)\
    .join(User_alias, org_members.c.user_id == User_alias.c.user_id_a)\
    .join(permissions_alias, role_permissions_alias.c.permission_id == permissions_alias.c.permission_id_a)\
    .join(ResourceAlias, permissions_alias.c.resource_id == ResourceAlias.c.resource_id_a)\
    .join(ActionAlias, permissions_alias.c.action_id == ActionAlias.c.action_id_a)

class OrgMemberPermission(db.Model):
    __table__ = org_member_permission_join
    user_id = org_members.c.user_id
    username = User_alias.c.username
    org_id = org_members.c.org_id
    resource = ResourceAlias.c.name_a
    action = ActionAlias.c.name

class OrgMemberPermissionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = OrgMemberPermission
    user_id = ma.auto_field()
    username = ma.auto_field()
    org_id = ma.auto_field()
    resource = ma.auto_field()
    action = ma.auto_field()

org_member_permission_schema = OrgMemberPermissionSchema()

