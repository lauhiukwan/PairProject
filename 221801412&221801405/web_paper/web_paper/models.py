from __init__ import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class UserCollection(db.Model):
    __tablename__ = "usercolletion"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    paper_id = db.Column(db.Integer)


class Paper(db.Model):
    __tablename__ = "paper"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    meeting = db.Column(db.String(10))
    url = db.Column(db.String(50))
    paper_abstract = db.Column(db.Text)
    date = db.Column(db.Date)


class PaperToKeyword(db.Model):
    __tablename__ = "papertokeyword"
    id = db.Column(db.Integer, primary_key=True)
    paper_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    keyword = db.Column(db.Text)

# class Role(db.Model):  # 继承数据库模型
#     # 定义表明
#     __tablename__ = 'role'
#     # dingyizhiduan
#     id = db.Column(db.Integer, primary_key=True)  # 表示是字段
#     # 创表语句
#     #加入这是一对多的关联表
#     #user= db.relationship('User')表示合User模型发生了关联，假装在Role里添加了一个user字段，仅仅是方便查询。
#     #user= db.relationship('User'，backref='role')定义了反向引用，在User里添加假装字段自己也有
#     #建立引用，外键直接使用role.user返回user对象
#     def __repr__(self):#可以用于打印数据，相当于类里的方法
#         return '<Role: %s>' % (self.id)
