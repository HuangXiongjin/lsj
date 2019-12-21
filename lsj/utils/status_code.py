# 成功
SUCCESS = (200, '操作成功', '添加上商品成功', '删除商品成功')
# 参数错误
ERROR_PARAM = (400, '参数错误')
# 资源找不到
ERROR_RESOUCE_NOT_FOUND = (404, '资源找寻失败')
# 内部服务器错误
ERROR_INTERNAL = (500, '系统正在繁忙')
# 用户名已存在
ERROR_USER_EXISTS = (4001, '用户名已存在')
# 密码不一致
ERROR_PASSWORD_DIFFERENT = (4002, '密码不一致')
# 用户名或密码错误
ERROR_USER_PASSWORD = (4003, '用户名或密码错误')
# 邮箱格式错误
ERROR_MOBILE = (4004, '无效的电话号码')
# 字段校验错误
ERROR_FIELD = (4005, '字段校验错误')
# 用户身份无效
ERROR_USER_INVALID = (4006, '请先去登录')

# access token过期
ERROR_ACCESS_TOKEN_EXPIRED = (4002, 'Access Token 过期')

# 违反唯一约束
ERROR_UNIQUE = (4004, '该手机号已被注册')
# 注册信息不完整
ERROR_REGISTER = (4005, '请选择用户身份', 4006, '请填写密码')
# 上传多次
ERROR_UPLOAD_UNIQUE = (4007, '不能多次上传作品')
# 评分违反唯一约束
ERROR_COMMENT_UNIQUE = (4008, '不能多次进行评分')
# 没有填写评分
ERROR_SCORE = (4009, '请填写分数')
# 文件类型无效
ERROR_FILE_TYPE = (5001, '文件类型无效')




