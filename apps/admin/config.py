# 配置文件 
'''
    设置菜单
    :param id:
        菜单id 和角色关联.
    :param pri_name:
        权限名称
    :param url_prefix:
        蓝图 或者 也可以成为模块名称
    :param actin_name:
        函数名称
'''
def set_menu(id,icon,pri_name,url_prefix,action_name,child_menu=[],is_treeview=True):
    menu = {'id':id,"icon":icon,'pri_name':pri_name,'url_prefix':url_prefix,'action_name':action_name,'is_treeview':is_treeview}
    if child_menu:
        menu['child']=child_menu
    return menu

menu = (
    set_menu(1,'fa fa-fw fa-paste (alias)','首页管理',None,None,child_menu=(
        set_menu(11,'fa fa-fw fa-copy (alias)','后台首页','adminindex','index',is_treeview=False),
    )),
    set_menu(5,'fa fa-fw fa-file','文章管理',None,None,child_menu=(
        set_menu(51,'fa fa-fw fa-tag','标签编辑','adminterms','edit?taxonomy=post_tag',is_treeview=False,child_menu=(
            set_menu(511,'','删除标签','adminterms','delete?taxonomy=post_tag'),
        )),
        set_menu(52,'fa fa-fw fa-folder-open','分类编辑','adminterms','edit?taxonomy=category',is_treeview=False,child_menu=(
            set_menu(511,'','删除分类','adminterms','delete?taxonomy=category'),
        )),
        set_menu(53,'fa fa-fw fa-book','文章管理','adminposts','index',is_treeview=False,child_menu=(
            set_menu(531,'','修改文章','adminposts','edit'),
            set_menu(532,'','新增文章','adminposts','add'),
            set_menu(533,'','删除文章','adminposts','delete'),
        )),
    )),
    set_menu(2,'fa fa-fw fa-user-plus','权限管理',None,None,child_menu=(
        set_menu(21,'fa fa-fw fa-user','管理员列表','adminadmin','index',child_menu=(
            set_menu(211,'','增加管理员','adminadmin','add'),
            set_menu(212,'','修改管理员','adminadmin','edit'),
            set_menu(213,'','删除管理员','adminadmin','delete'),
        ),is_treeview=False),
        set_menu(22, 'fa fa-fw fa-user-secret','角色列表', 'adminrole', 'index', child_menu=(
            set_menu(221,'', '增加角色', 'adminrole', 'add'),
            set_menu(222,'', '修改角色', 'adminrole', 'edit'),
            set_menu(223,'', '删除角色', 'adminrole', 'delete'),
        ),is_treeview=False),

    )),
    set_menu(3,'fa fa-fw fa-wrench','系统管理',None,None,child_menu=(
        set_menu(31,'fa fa-fw fa-legal (alias)','系统配置字段', 'adminconfig_field', 'index', child_menu=(
            set_menu(311,'', '增加配置字段', 'adminconfig_field', 'add'),
            set_menu(312,'','修改配置字段', 'adminconfig_field', 'edit'),
            set_menu(313,'','删除配置字段', 'adminconfig_field', 'delete'),
        ),is_treeview=False),
        set_menu(32,'fa fa-fw fa-sticky-note-o','网站设置', 'adminconfig_field', 'web',is_treeview=False),
        set_menu(33,'fa fa-fw fa-cloud-upload','上传设置', 'adminconfig_field', 'up', is_treeview=False),
        set_menu(34,'fa fa-fw fa-folder-o' ,'日志列表', 'adminlog', 'index', child_menu=(
            set_menu(341,'','删除日志', 'adminlog', 'delete'),
            set_menu(342,'','删除缓存', 'adminindex', 'clear_cache'),
        ),is_treeview=False),
        set_menu(35,'fa fa-fw fa-eraser','菜单管理', 'adminterms', 'menu', is_treeview=False),
    )),
    set_menu(4,'fa fa-fw fa-database','数据库管理','','',child_menu=(
        set_menu(41,'fa fa-fw fa-list-alt','数据库表', 'admindatabase', 'index',child_menu=(
            set_menu(411,'','备份数据表', 'admindatabase', 'backup'),
        ),is_treeview=False),
    set_menu(42,'fa fa-fw fa-reply','还原数据库列表', 'admindatabase', 'reduction',child_menu=(
            set_menu(421,'','下载备份', 'admindatabase', 'dowonload'),
            set_menu(422,'','还原数据库', 'admindatabase', 'restore'),
            set_menu(423,'','删除数据库', 'admindatabase', 'delete'),
        ),is_treeview=False),
    ))
)

role_type = {1:'超级管理员',2:'普通管理员'}

# 登录成功session 记录标记
ADMIN_SESSION_ID = 'a6273a8b622104d4d63d0'

# 分页大小
PAGE_SIZE = 15

# tb_term_taxonomy表 taxonomy 字段 枚举
TAXONOMY = {"category":1,"post_tag":2,"nav_menu":3}

TAXONOMY_CN = {'category':'分类','post_tag':'标签','nav_menu':'菜单'}
POST_TYPE = {"普通文章":1,"单页":2}




